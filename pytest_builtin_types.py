"""Provide Builtin Types for Testing in other pytest tests"""

import pytest
from typing import TypedDict, List, Tuple, Set, Dict, Union

# Typing
_BasicList = List[Union[str, int, float, bool]]
_BasicTuple = Tuple[Union[str, int, float, bool]]
_BasicSet = Set[Union[str, int, float, bool]]
_BasicTypes = TypedDict("_BasicTypes", {str: str, int: int, float: float, bool: bool})
_BasicContainers = TypedDict(
    "_BasicContainers", {list: List, tuple: Tuple, set: Set, dict: Dict, bool: bool}
)

_AllBasicTypes = TypedDict(
    "_AllBasicTypes",
    {
        str: str,
        int: int,
        float: float,
        list: List,
        tuple: Tuple,
        set: Set,
        dict: Dict,
        bool: bool,
    },
)
# Constants
_BOOL_1: bool = True
_BOOL_2: bool = False

_FLOAT_1: float = 1.1
_FLOAT_2: float = 1.2

_INT_1: int = 1
_INT_2: int = 2

_STRING_1: str = "string1"
_STRING_2: str = "string2"

_MULTILINE_1: str = """Multiline1\nTest1\n\n"""
_MULTILINE_2: str = """Multiline2\nTest2\n\n"""

_BASIC_TYPES_1: _BasicTypes = {
    str: _STRING_1,
    int: _INT_1,
    float: _FLOAT_1,
    bool: _BOOL_1,
}
_BASIC_TYPES_2: _BasicTypes = {
    str: _STRING_2,
    int: _INT_2,
    float: _FLOAT_2,
    bool: _BOOL_2,
}

_LIST_1: _BasicList = list(value for value in _BASIC_TYPES_1.values())
_LIST_2: _BasicList = list(value for value in _BASIC_TYPES_2.values())

_SET_1: _BasicSet = set(value for value in _BASIC_TYPES_1.values())
_SET_2: _BasicSet = set(value for value in _BASIC_TYPES_2.values())

_TUPLE_1: _BasicTuple = tuple(value for value in _BASIC_TYPES_1.values())
_TUPLE_2: _BasicTuple = tuple(value for value in _BASIC_TYPES_2.values())

_BASIC_CONTAINERS_1: _BasicContainers = {
    list: _LIST_1,
    tuple: _TUPLE_1,
    set: _SET_1,
    dict: _BASIC_TYPES_1,
}
_BASIC_CONTAINERS_2: _BasicContainers = {
    list: _LIST_2,
    tuple: _TUPLE_2,
    set: _SET_2,
    dict: _BASIC_TYPES_2,
}

_ALL_BASIC_TYPES_1: _AllBasicTypes = {**_BASIC_TYPES_1, **_BASIC_CONTAINERS_1}
_ALL_BASIC_TYPES_2: _AllBasicTypes = {**_BASIC_TYPES_2, **_BASIC_CONTAINERS_2}


@pytest.fixture
def float_1() -> float:
    """Returns a float"""
    return _FLOAT_1


@pytest.fixture
def float_2() -> float:
    """Returns a float"""
    return _FLOAT_2


@pytest.fixture
def int_1() -> int:
    """Returns int"""
    return _INT_1


@pytest.fixture
def int_2() -> int:
    """Returns int"""
    return _INT_2


@pytest.fixture
def string_1() -> str:
    """Returns str"""
    return _STRING_1


@pytest.fixture
def string_2() -> str:
    """Returns str"""
    return _STRING_2


@pytest.fixture
def multiline_1() -> str:
    """Returns str"""
    return _MULTILINE_1


@pytest.fixture
def multiline_2() -> str:
    """Returns str"""
    return _MULTILINE_2


@pytest.fixture
def basic_types_1() -> _BasicTypes:
    """Returns a mapping of basic types"""
    return _BASIC_TYPES_1


@pytest.fixture
def basic_types_2() -> _BasicTypes:
    """Returns a mapping of basic types"""
    return _BASIC_TYPES_2


@pytest.fixture
def list_1() -> _BasicList:
    """Returns a basic list with values"""
    return _LIST_1


@pytest.fixture
def list_2() -> _BasicList:
    """Returns a basic list with values"""
    return _LIST_2


@pytest.fixture
def set_1() -> _BasicSet:
    """Returns a basic set with values"""
    return _SET_1


@pytest.fixture
def set_2() -> _BasicSet:
    """Returns a basic set with values"""
    return _SET_2


@pytest.fixture
def tuple_1() -> _BasicTuple:
    """Returns a basic tuple with values"""
    return _TUPLE_1


@pytest.fixture
def tuple_2() -> _BasicTuple:
    """Returns a basic tuple with values"""
    return _TUPLE_2


@pytest.fixture
def basic_types_1() -> _BasicTypes:
    """Returns a dictionary of basic types with values"""
    return _BASIC_TYPES_1


@pytest.fixture
def basic_types_2() -> _BasicTypes:
    """Returns a dictionary of basic types with values"""
    return _BASIC_TYPES_2


@pytest.fixture
def basic_containers_1() -> _BasicContainers:
    """Returns a dictionary of basic containers with values"""
    return _BASIC_CONTAINERS_1


@pytest.fixture
def basic_containers_2() -> _BasicContainers:
    """Returns a dictionary of basic containers with values"""
    return _BASIC_CONTAINERS_2


@pytest.fixture
def all_basic_types_1() -> _AllBasicTypes:
    """Dictionary of all the basic containers and types with values"""
    return _ALL_BASIC_TYPES_1


@pytest.fixture
def all_basic_types_2() -> _AllBasicTypes:
    """Dictionary of all the basic containers and types with values"""
    return _ALL_BASIC_TYPES_2


@pytest.fixture(params=[*_LIST_1])
def parametrized_basic_types_1(request):
    """parametrized fixture of basic types with values"""
    return request.param


@pytest.fixture(params=[*_LIST_2])
def parametrized_basic_types_2(request):
    """parametrized fixture of basic types with values"""
    return request.param


@pytest.fixture(params=[value for value in _BASIC_CONTAINERS_1.values()])
def parametrized_basic_containers_1(request):
    """parametrized fixture of basic containers with values"""
    return request.param


@pytest.fixture(params=[value for value in _BASIC_CONTAINERS_2.values()])
def parametrized_basic_containers_2(request):
    """parametrized fixture of basic containers with values"""
    return request.param


@pytest.fixture(params=[value for value in _ALL_BASIC_TYPES_1.values()])
def parametrized_all_basic_types_1(request):
    """parametrized fixture of basic containers and types with values"""
    return request.param


@pytest.fixture(params=[value for value in _ALL_BASIC_TYPES_2.values()])
def parametrized_all_basic_types_2(request):
    """parametrized fixture of basic containers and types with values"""
    return request.param
