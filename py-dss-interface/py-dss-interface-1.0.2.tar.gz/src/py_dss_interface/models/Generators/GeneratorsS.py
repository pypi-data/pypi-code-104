# -*- encoding: utf-8 -*-
"""
 Created by eniocc at 11/10/2020
"""
import ctypes

from py_dss_interface.models.Base import Base


class GeneratorsS(Base):
    """
    This interface can be used to read/write certain properties of the active DSS object.

    The structure of the interface is as follows:
        CStr GeneratorsS(int32_t Parameter, CStr Argument);

    This interface returns a string as a result of the query according to the value of the variable Parameter,
    which can be one of the following.
    """

    def generators_read_name(self) -> str:
        """Gets the name of the active Generator."""
        result = ctypes.c_char_p(self.dss_obj.GeneratorsS(ctypes.c_int32(0), ctypes.c_int32(0)))
        return result.value.decode('ascii')

    def generators_write_name(self, argument: str) -> str:
        """Sets the name of the active Generator."""
        result = ctypes.c_char_p(self.dss_obj.GeneratorsS(ctypes.c_int32(1), argument.encode('ascii')))
        return result.value.decode('ascii')
