from typing import Any, Dict

from myst.models import base_model


class OperationGetInputSpecsSchema(base_model.BaseModel):
    """A JSON Schema definition describing the inputs that this operation can be used with."""

    __root__: Dict[str, Any]

    def __getitem__(self, item: str) -> Any:
        return self.__root__[item]
