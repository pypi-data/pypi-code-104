# automatically generated by the FlatBuffers compiler, do not modify

# namespace: fbs

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class Shape(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsShape(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Shape()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def ShapeBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x4F\x52\x54\x4D", size_prefixed=size_prefixed)

    # Shape
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Shape
    def Dim(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from ort_flatbuffers_py.fbs.Dimension import Dimension
            obj = Dimension()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Shape
    def DimLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Shape
    def DimIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        return o == 0

def ShapeStart(builder): builder.StartObject(1)
def ShapeAddDim(builder, dim): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(dim), 0)
def ShapeStartDimVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def ShapeEnd(builder): return builder.EndObject()
