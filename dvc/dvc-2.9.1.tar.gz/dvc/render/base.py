import abc
from typing import TYPE_CHECKING, Dict

from dvc.exceptions import DvcException

if TYPE_CHECKING:
    from dvc.types import StrPath


REVISION_FIELD = "rev"
INDEX_FIELD = "step"


class BadTemplateError(DvcException):
    pass


class Renderer(abc.ABC):
    def __init__(self, data: Dict, templates=None):
        self.data = data
        self.templates = templates

        from dvc.render.utils import get_files

        files = get_files(self.data)

        # we assume comparison of same file between revisions for now
        assert len(files) == 1
        self.filename = files.pop()

    def _convert(self, path: "StrPath"):
        raise NotImplementedError

    @property
    @abc.abstractmethod
    def DIV(self):
        raise NotImplementedError

    @property
    @abc.abstractmethod
    def SCRIPTS(self):
        raise NotImplementedError

    @abc.abstractmethod
    def as_json(self):
        raise NotImplementedError

    @staticmethod
    def _remove_special_chars(string: str):
        return string.translate(
            {ord(c): "_" for c in r"!@#$%^&*()[]{};,<>?\/:.|`~=_+"}
        )

    def generate_html(self, path: "StrPath"):
        """this method might edit content of path"""
        partial = self._convert(path)

        div_id = self._remove_special_chars(self.filename)
        div_id = f"plot_{div_id}"

        return self.DIV.format(id=div_id, partial=partial)
