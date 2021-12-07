# coding=utf-8
# Copyright 2021 The Balloon Learning Environment Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""A variational autoencoder (VAE) for generating wind fields."""

import dataclasses
from typing import NamedTuple, Tuple

from flax import linen as nn
import jax
import jax.numpy as jnp


@dataclasses.dataclass
class FieldShape:
  """Class to parameterize the shape of the VAE field."""

  latlng_slices: int = 21
  flow_field_width: int = 7
  pressure_slices: int = 10
  time_slices: int = 9

  latlng_displacement_km: float = 500.
  max_pressure_pa: float = 14000.
  min_pressure_pa: float = 5000.
  time_horizon_hours: int = 48

  def direction_grid_shape(self) -> Tuple[int, int, int, int]:
    """Returns the shape of the grid for an individual u or v field."""

    return (self.latlng_slices, self.latlng_slices, self.pressure_slices,
            self.time_slices)

  def grid_shape(self) -> Tuple[int, int, int, int, int]:
    """Returns the shape of the grid for combined u and v field."""

    # NOTE(scandido): Last dimension is u, v.
    return (self.latlng_slices, self.latlng_slices, self.pressure_slices,
            self.time_slices, 2)

  def num_grid_points(self) -> int:
    """Returns the number of points in the grid."""

    return (self.latlng_slices * self.latlng_slices * self.pressure_slices *
            self.time_slices)

  def output_length(self) -> int:
    """Returns the number of outputs of the field."""

    # NOTE(scandido): Each grid point will have u and v fields, so the number of
    # parameters for the field is 2x the number of grid points.
    return 2 * self.num_grid_points()

  def num_flow_fields(self) -> int:
    """Returns the number of flow fields generated by the decoder."""

    return self.pressure_slices * self.time_slices

  def num_flow_field_units(self) -> int:
    """Returns the number of flow field outputs used in the decoder."""

    return (self.flow_field_width * self.flow_field_width *
            self.num_flow_fields())

  def latlng_grid_points(self) -> jnp.ndarray:
    """Returns the 1D grid points for latitude or longitude axes."""

    return jnp.linspace(-self.latlng_displacement_km,
                        self.latlng_displacement_km, self.latlng_slices)

  def pressure_grid_points(self) -> jnp.ndarray:
    """Returns the 1D grid points for the pressure axis."""

    return jnp.linspace(self.min_pressure_pa, self.max_pressure_pa,
                        self.pressure_slices)

  def time_grid_points(self) -> jnp.ndarray:
    """Returns the 1D grid points for the time axis."""

    return jnp.linspace(0, self.time_horizon_hours, self.time_slices,
                        dtype=jnp.int32)


class EncoderOutput(NamedTuple):
  mean: jnp.ndarray
  logvar: jnp.ndarray


class VAEOutput(NamedTuple):
  reconstruction: jnp.ndarray
  encoder_output: EncoderOutput
  sigma: float


@jax.jit
def _squash(x: jnp.ndarray, cap: float = 50) -> jnp.ndarray:
  """Saturates signal to the [-1, 1] range."""

  s = jnp.sign(x)
  x = jnp.abs(x)
  return s * x / (cap + x)


class Encoder(nn.Module):
  """An encoder network for a variational autoencoder."""
  num_latents: int
  num_hidden_layers: int = 3
  hidden_layer_network_width: int = 1000

  @nn.compact
  def __call__(self, x: jnp.ndarray) -> EncoderOutput:
    x = _squash(x.ravel())
    for _ in range(self.num_hidden_layers):
      x = nn.Dense(self.hidden_layer_network_width)(x)
      x = nn.relu(x)

    mean_x = nn.Dense(self.num_latents, name='mean')(x)
    logvar_x = nn.Dense(self.num_latents, name='logvar')(x)
    return EncoderOutput(mean_x, logvar_x)


class Decoder(nn.Module):
  """A decoder network for a variational autoencoder."""
  num_hidden_layers: int = 3
  hidden_layer_network_width: int = 1000
  field_shape: FieldShape = FieldShape()

  @nn.compact
  def __call__(self, z: jnp.ndarray) -> jnp.ndarray:
    for _ in range(self.num_hidden_layers):
      z = nn.Dense(self.hidden_layer_network_width)(z)
      z = nn.relu(z)
    z = nn.Dense(self.field_shape.num_flow_field_units())(z)

    # Chunk up the MLP portion of the decoder's output into flow fields for
    # each pressure level of each time slice.
    flow_fields = z.reshape((self.field_shape.flow_field_width,
                             self.field_shape.flow_field_width,
                             self.field_shape.num_flow_fields()))

    # Expand each flow field into NxN arrays. We construct smaller flow fields Ψ
    # because it makes the process less compute intensive and forces the flow
    # field to not have high frequency content that prevents us from getting
    # a smooth output field.
    # NOTE(scandido): We grow the flow fields with a buffer of +2 (1 pixel
    # border around the field) so we don't need to worry about the boundary
    # of the difference equations below.
    flow_fields = jax.image.resize(
        flow_fields,
        (self.field_shape.latlng_slices + 2, self.field_shape.latlng_slices + 2,
         self.field_shape.num_flow_fields()),
        method='linear')

    # Now create incompressible wind fields by differentiating the flow field.
    # NOTE(scandido): In principle we'd need to take into account the size of
    # the grid (in the denominator, 2 * 𝝙x) but since we're learning to generate
    # Ψ via a deep network this parameter is learned via modulation of the
    # magnitude of Ψ and we can avoid additional parameterization here.
    dflow_dy = (jnp.roll(flow_fields, shift=-1, axis=0) -
                jnp.roll(flow_fields, shift=1, axis=0)) / 2.
    dflow_dy = dflow_dy[1:-1, 1:-1, :]
    dflow_dx = (jnp.roll(flow_fields, shift=-1, axis=1) -
                jnp.roll(flow_fields, shift=1, axis=1)) / 2.
    dflow_dx = dflow_dx[1:-1, 1:-1, :]

    # Reshape the fields into pressure levels within time slices.
    # NOTE(scandido): We don't much care what decoder MLP outputs correspond to
    # which pressure-time slices or how things are ordered here because the
    # mapping is all learned in training so we optimize the code readability.
    u_fields = dflow_dy.reshape(*self.field_shape.direction_grid_shape())
    v_fields = -1 * dflow_dx.reshape(*self.field_shape.direction_grid_shape())

    # Stick together the 4D field by stacking everything.
    return jnp.stack([u_fields, v_fields], axis=-1)


# fields elsewhere (eventually).
class WindFieldVAE(nn.Module):
  """Class that learns a VAE to generate wind fields."""
  num_latents: int = 64
  reparameterize_latents: bool = True
  field_shape: FieldShape = FieldShape()

  def setup(self):
    self.encoder = Encoder(self.num_latents)
    self.decoder = Decoder()
    self.sigma = self.variable('params', 'sigma', lambda: 1.)

  def __call__(self, x: jnp.ndarray, z_rng: jnp.ndarray) -> VAEOutput:
    encoder_out = self.encoder(x)

    if self.reparameterize_latents:
      z = self._reparameterize(z_rng, encoder_out.mean, encoder_out.logvar)
    else:
      z = encoder_out.mean

    y = self.decoder(z)
    return VAEOutput(y, encoder_out, self.sigma.value)

  def generate(self, z: jnp.ndarray) -> jnp.ndarray:
    return self.decoder(z)

  @staticmethod
  def _reparameterize(
      rng: jnp.ndarray, mean: jnp.ndarray, logvar: jnp.ndarray) -> jnp.ndarray:
    std = jnp.exp(0.5 * logvar)
    eps = jax.random.normal(rng, logvar.shape)
    return mean + eps * std


def model():
  return WindFieldVAE()
