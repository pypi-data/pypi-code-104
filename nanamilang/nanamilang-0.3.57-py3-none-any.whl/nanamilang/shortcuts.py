"""NanamiLang Shortcuts"""

# This file is a part of NanamiLang Project
# This project licensed under GNU GPL version 2
# Initially made by @jedi2light (aka Stoian Minaiev)

import functools
import random
import string
from typing import Any


def get(coll: tuple, idx: int, _def):
    """Safely get value from coll"""

    try:
        return coll[idx]
    except IndexError:
        return None or _def


def find(coll, default, element=None, function=None):
    """Safely find an element in coll  using filter"""

    if not function:
        if not element:
            return None or default
        # Pylint, babeee, pleeeeease...
        function = lambda e: e == element

    return get(tuple(filter(function, coll)), 0, default)


def enpart(coll: tuple or list) -> tuple:
    """Turn collection into partitioned"""

    return tuple(coll[i:i + 2] for i in range(0, len(coll), 2))


def depart(coll: tuple or list) -> tuple:
    """Return partitioned into collection"""

    return functools.reduce(lambda e, n: e + n, coll or ((None,),))


def randstr(length: int = 10) -> str:
    """Return randomly generated string"""

    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))


########################################################################################################################


def ASSERT_COLL_LENGTH_IS(coll: list or tuple or set, length: int, message: str = '') -> None:
    """ASSERT_COLL_LENGTH_IS: whether collection length equals to or not?"""
    assert isinstance(coll, (list, tuple, set)), 'ASSERT_COLL_LENGTH_IS: not a list, set or tuple'
    assert len(coll) == length, message or f'collection length does not equal to {length}'


def ASSERT_COLL_LENGTH_IS_EVEN(coll: list or tuple or set, message: str = '') -> None:
    """ASSERT_COLL_LENGTH_IS_EVEN: whether collection length is even or not?"""
    assert isinstance(coll, (list, tuple, set)), 'ASSERT_COLL_LENGTH_IS_EVEN: not a list, set or tuple'
    assert len(coll) % 2 == 0, message or 'collection length must be even'


########################################################################################################################


def ASSERT_COLLECTION_IS_NOT_EMPTY(collection: Any, message: str = '') -> None:
    """ASSERT_COLLECTION_IS_NOT_EMPTY: whether collection (or string) empty or not?"""
    assert hasattr(collection, '__len__'), 'ASSERT_COLLECTION_IS_NOT_EMPTY: has no __len__'
    assert len(collection) > 0, message or 'collection (or string) could not be empty'


########################################################################################################################


def ASSERT_NO_DUPLICATES(coll: list or tuple or set, message: str = '') -> None:
    """ASSERT_NO_DUPLICATES: does the list contain duplicates?"""
    assert isinstance(coll, (list, tuple, set)), 'ASSERT_NO_DUPLICATES: not a list, set or tuple'
    assert len(coll) == len(set(coll)), message or 'collection could not contain duplicates'


########################################################################################################################


def ASSERT_DICT_CONTAINS_KEY(key: Any, dct: dict, message: str = '') -> None:
    """ASSERT_DICT_CONTAINS_KEY: does the dict keys contain key?"""
    assert isinstance(dct, dict), 'ASSERT_DICT_CONTAINS_KEY: not a dict'
    assert key in dct.keys(), message or f'dictionary does not contain "{key}" key'


def ASSERT_COLL_CONTAINS_ELEMENT(elem: Any, coll: list or tuple or set, message: str = '') -> None:
    """ASSERT_COLL_CONTAINS_ELEMENT: does the coll contain element?"""
    assert isinstance(coll, (list, tuple, set)), 'ASSERT_COLL_CONTAINS_ELEMENT: not a list, set or tuple'
    assert elem in coll, message or f'collection does not contain "{elem}", valid values are: "{coll}"'


########################################################################################################################


def ASSERT_IS_INSTANCE_OF(inst: Any, of: Any, message: str = '') -> None:
    """ASSERT_IS_INSTANCE_OF: whether given instance is actually instance of ...?"""
    assert isinstance(inst, of), message or f'must be an instance of {of.__name__}"'


def ASSERT_IS_CHILD_OF(inst: Any, of: Any, message: str = '') -> None:
    """ASSERT_IS_CHILD_OF: whether given instance is actually child of ...?"""
    assert issubclass(inst.__class__, (of,)), message or f'must be an child of {of.__name__}"'


########################################################################################################################


def ASSERT_EVERY_COLLECTION_ITEM_EQUALS_TO(coll: list or tuple or set, to: Any, message: str = '') -> None:
    """ASSERT_EVERY_COLLECTION_ITEM_EQUALS_TO: does every collection item equal to ...?"""
    assert isinstance(coll, (list, tuple, set)), 'ASSERT_EVERY_COLLECTION_ITEM_EQUALS_TO: not a list, set or tuple'
    assert len(list(filter(lambda x: x == to, coll))) == len(coll), message or (
        f'every collection item must be equal to {to.__name__}'
    )


def ASSERT_EVERY_COLLECTION_ITEM_IS_CHILD_OF(coll: list or tuple or set, of: Any, message: str = '') -> None:
    """ASSERT_EVERY_COLLECTION_ITEM_IS_CHILD_OF: does every collection item is a child of ...?"""
    assert isinstance(coll, (list, tuple, set)), 'ASSERT_EVERY_COLLECTION_ITEM_IS_CHILD_OF: not a list, set or tuple'
    assert len(list(filter(lambda x: issubclass(x.__class__, (of,)), coll))) == len(coll), message or (
        f'every collection item must be an instance of {of.__name__}'
    )


def ASSERT_EVERY_COLLECTION_ITEM_IS_INSTANCE_OF(coll: list or tuple or set, of: Any, message: str = '') -> None:
    """ASSERT_EVERY_COLLECTION_ITEM_IS_INSTANCE_OF: does every collection item is an instance of ...?"""
    assert isinstance(coll, (list, tuple, set)), 'ASSERT_EVERY_COLLECTION_ITEM_IS_INSTANCE_OF: not a list. set or tuple'
    assert len(list(filter(lambda x: isinstance(x, of), coll))) == len(coll), message or (
        f'every collection item must be an instance of {of.__name__}'
    )


########################################################################################################################


def UNTERMINATED_SYMBOL(sym: str, m: str = ''):
    """UNTERMINATED_SYMBOL(sym) -> message"""
    return m or f'Encountered an unterminated \'{sym}\' symbol'


def UNTERMINATED_SYMBOL_AT_EOF(sym: str, m: str = ''):
    """UNTERMINATED_SYMBOL_AT_EOF(sym) -> message"""
    return m or f'Encountered an unterminated symbol \'{sym}\' symbol at the end of file'

########################################################################################################################
