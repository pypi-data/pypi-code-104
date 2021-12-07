__author__ = "Tomasz Rybotycki"

"""
    This class should be used as a base class for all standard BS permanent calculators.
    By standard I mean that the matrix and in(out)put states are stored in a variables.
    It takes care of a lot of boilerplate code.
"""

from typing import Optional

from numpy import ndarray, int64, array, asarray

from ..permanent_calculators.bs_permanent_calculator_interface import BSPermanentCalculatorInterface


class BSPermanentCalculatorBase(BSPermanentCalculatorInterface):

    def __init__(self, matrix: ndarray, input_state: Optional[ndarray] = None,
                 output_state: Optional[ndarray] = None) -> None:
        if output_state is None:
            output_state = array([], dtype=int64)
        if input_state is None:
            input_state = array([], dtype=int64)
        self._matrix = matrix
        self._input_state = input_state
        self._output_state = output_state

    @property
    def matrix(self) -> ndarray:
        return self._matrix

    @matrix.setter
    def matrix(self, matrix: ndarray) -> None:
        self._matrix = matrix

    @property
    def input_state(self) -> ndarray:
        return self._input_state

    @input_state.setter
    def input_state(self, input_state: ndarray) -> None:
        self._input_state = asarray(input_state, dtype=int64)

    @property
    def output_state(self) -> ndarray:
        return self._output_state

    @output_state.setter
    def output_state(self, output_state: ndarray) -> None:
        self._output_state = asarray(output_state, dtype=int64)

    def _can_calculation_be_performed(self) -> bool:
        """
            Checks if calculation can be performed. For this to happen sizes of given
            matrix and states have to match.

            :return: Information if the calculation can be performed.
        """
        return self._matrix.shape[0] == self._matrix.shape[1] \
            and len(self._output_state) == len(self._input_state) \
            and len(self._output_state) <= self._matrix.shape[0]
