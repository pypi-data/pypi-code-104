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

"""Balloon Learning Environment.

This provides the RL layer on top of the simulator.
"""

import math
import time
from typing import Any, Callable, Mapping, Optional, Text, Tuple, Union

from balloon_learning_environment.env import balloon_arena
from balloon_learning_environment.env import features
from balloon_learning_environment.env import generative_wind_field  # pylint: disable=unused-import
from balloon_learning_environment.env import simulator_data
from balloon_learning_environment.env import wind_field
from balloon_learning_environment.env.balloon import balloon
from balloon_learning_environment.env.balloon import control
from balloon_learning_environment.env.balloon import standard_atmosphere
from balloon_learning_environment.env.rendering import renderer as randerer_lib
from balloon_learning_environment.utils import transforms
from balloon_learning_environment.utils import units
from flax.metrics import tensorboard
import gin
import gym
import jax
import numpy as np


@gin.configurable
class BalloonEnv(gym.Env):
  """Balloon Learning Environment.

  Observations returned by this environment are 3 dimensional
        numpy arrays with the following format:
        0-1: balloon's x, y position in km.
        2: and the baloon's pressure level in kPa.
  """

  def __init__(
      self,
      *,  # All arguments after this are keyword-only.
      station_keeping_radius_km: float = 50.0,
      reward_dropoff: float = 0.4,
      reward_halflife: float = 100.0,
      arena: Optional[balloon_arena.BalloonArenaInterface] = None,
      feature_constructor_factory: Callable[
          [wind_field.WindField, standard_atmosphere.Atmosphere],
          features.FeatureConstructor] = features.PerciatelliFeatureConstructor,
      wind_field_factory: Callable[
          [], wind_field.WindField] = generative_wind_field.GenerativeWindField,
      seed: Optional[int] = None,
      renderer: Optional[randerer_lib.Renderer] = None):
    """Constructs a Balloon Learning Environment Station Keeping Environment.

    The reward function for the environment returns 1.0 when the balloon is
    with the station keeping radius, and roughly:
      reward_dropoff * 2^(-distance_from_radius / reward_halflife)
    when outside the station keeping radius. That is, the reward immediately
    outside the station keeping radius is reward_dropoff, and the reward
    decays expontentially as the balloon moves further from the radius.

    Args:
      station_keeping_radius_km: The desired station keeping radius in km. When
        the balloon is within this radius, the reward is 1.0.
      reward_dropoff: The reward multiplier for when the balloon is outside of
        station keeping range. See reward definition above.
      reward_halflife: The half life of the reward function. See reward
        definition above.
      arena: A balloon arena (simulator) to wrap. If set to None, it will use
        the default balloon arena.
      feature_constructor_factory: A callable which returns a new
        FeatureConstructor object when called. The factory takes a forecast
        (WindField) and an initial observation from the simulator
        (SimulatorObservation).
      wind_field_factory: A callable which returns a new WindField object.
      seed: A PRNG seed for the environment.
      renderer: An optional renderer for rendering flight paths/simulator state.
    """
    self.radius = units.Distance(km=station_keeping_radius_km)
    self._reward_dropoff = reward_dropoff
    self._reward_halflife = reward_halflife
    self._feature_constructor_factory = feature_constructor_factory
    self._global_iteration = 0
    self.summary_writer = None

    if arena is None:
      self.arena = balloon_arena.BalloonArena(self._feature_constructor_factory,
                                              wind_field_factory())
    else:
      self.arena = arena

    self._renderer = renderer
    if renderer is not None:
      self.metadata = {'render.modes': self._renderer.render_modes}

    # Use time in microseconds if a seed is not supplied.
    self.seed(seed if seed is not None else int(time.time() * 1e6))
    self.reset()

  def step(self,
           action: int) -> Tuple[np.ndarray, float, bool, Mapping[str, Any]]:
    """Applies an action and steps the environment.

    Args:
      action: An integer action corresponding to AlititudeControlCommand in
        env/balloon.py.

    Returns:
      An (observation, reward, terminal, info) tuple.

    Raises:
      RuntimeError: If reset is not called at least once before step.
    """
    command = control.AltitudeControlCommand(action)
    observation = self.arena.step(command)
    assert isinstance(observation, np.ndarray)

    if self._renderer is not None:
      self._renderer.step(self.arena.get_simulator_state())

    # Prepare reward
    reward = self._calculate_reward()

    # Prepare is_terminal
    balloon_state = self.arena.get_balloon_state()
    out_of_power = balloon_state.status == balloon.BalloonStatus.OUT_OF_POWER
    envelope_burst = (
        balloon_state.status == balloon.BalloonStatus.BURST)
    zeropressure = (
        balloon_state.status == balloon.BalloonStatus.ZEROPRESSURE)
    is_terminal = out_of_power or envelope_burst or zeropressure

    self._gather_summaries(action)
    self._global_iteration += 1

    return observation, reward, is_terminal, {
        'out_of_power': out_of_power,
        'envelope_burst': envelope_burst,
        'zeropressure': zeropressure,
        'time_elapsed': balloon_state.time_elapsed}

  def reset(self) -> np.ndarray:
    self._rng, arena_rng = jax.random.split(self._rng)
    observation = self.arena.reset(arena_rng)

    if self._renderer is not None:
      self._renderer.reset()
      self._renderer.step(self.arena.get_simulator_state())

    return observation

  def render(self, mode: str = 'human') -> Union[None, np.ndarray, Text]:
    """Renders a frame.

    Args:
      mode: One of `human`, `rgb_array`, `ansi`, or `tensorboard`. `human`
        corresponds to rendering directly to the screen. `rgb_array` renders to
        a numpy array and returns it. `ansi` renders to a string or StringIO
        object. `tensorboard` renders the images on tensorboard (if that
        collector is active).

    Returns:
      None, a numpy array of rgb data, or a Text object, depending on the mode.

    Raises:
      ValueError: Propagated from the internal renderer if mode is not in
        self.metadata['render.modes'] i.e. not implemented in the renderer.
    """
    if self._renderer is None:
      return None

    if mode == 'tensorboard':
      return self._renderer.render(
          mode, self.summary_writer, self._global_iteration)

    return self._renderer.render(mode)

  def close(self) -> None:
    # Nothing to cleanup.
    pass

  def seed(self, seed: int) -> None:
    self._rng = jax.random.PRNGKey(seed)

  @property
  def unwrapped(self) -> gym.Env:
    return self

  @property
  def action_space(self) -> gym.spaces.Discrete:
    return gym.spaces.Discrete(3)

  @property
  def observation_space(self) -> gym.Space:
    return self.arena.feature_constructor.observation_space

  @property
  def reward_range(self) -> Tuple[float, float]:
    return (0.0, 1.0)

  def get_simulator_state(self) -> simulator_data.SimulatorState:
    return self.arena.get_simulator_state()

  def _calculate_reward(self) -> float:
    balloon_state = self.arena.get_balloon_state()
    x, y = balloon_state.x, balloon_state.y

    # x, y are in meters.
    distance = units.relative_distance(x, y)

    # Base reward - distance to station keeping radius.
    if distance <= self.radius:
      # Reward is 1.0 within the radius.
      reward = 1.0
    else:
      # Exponential decay outside boundary with drop
      # ln(0.5) is approximately -0.69314718056.
      reward = self._reward_dropoff * math.exp(
          -0.69314718056 / self._reward_halflife *
          (distance - self.radius).kilometers)

    # Power regularization. Only applied when using more power (going down)
    # and there isn't excess energy available.
    if (balloon_state.last_command == control.AltitudeControlCommand.DOWN and
        not balloon_state.excess_energy):
      max_multiplier = 0.95
      penalty_skew = 0.3
      scale = transforms.linear_rescale_with_saturation(
          balloon_state.acs_power.watts, 100.0, 300.0)
      multiplier = max_multiplier - penalty_skew * scale
      reward *= multiplier

    # TODO(joshgreaves): Add negative penalty for terminal state.

    return reward

  def __str__(self) -> str:
    return 'SleewpalkEnv'

  def __enter__(self) -> gym.Env:
    return self

  def __exit__(self, *args: Any) -> bool:
    self.close()
    return False  # Reraise any exceptions

  def set_summary_writer(
      self, summary_writer: Optional[tensorboard.SummaryWriter]) -> None:
    self.summary_writer = summary_writer

  # TODO(psc): This shouldn't be done here. Modify this so it is passed back to
  # the dispatcher (which passes it to the collectors).
  def _gather_summaries(self, action: int):
    """If summary_writer is available, gather summaries from BalloonArena."""
    if self.summary_writer is None:
      return

    self.summary_writer.scalar('Balloon/Actions', action,
                               self._global_iteration)
    self.arena.get_summaries(self.summary_writer, self._global_iteration)
    self.render(mode='tensorboard')


gym.register(
    id='BalloonLearningEnvironment-v0',
    entry_point='balloon_learning_environment.env.balloon_env:BalloonEnv')
