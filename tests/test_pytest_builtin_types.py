"""Testing pytest_builtin_types"""
from pytest_builtin_types import *
from pytest_builtin_types import (
    _BasicTypes,
    _BasicContainers,
    _BasicTuple,
    _AllBasicTypes,
    _BasicList,
    _BasicSet,
    _BASIC_TYPES_1,
    _BASIC_TYPES_2,
    _ALL_BASIC_TYPES_1,
    _ALL_BASIC_TYPES_2,
    _INT_1,
    _INT_2,
    _SET_1,
    _SET_2,
    _STRING_2,
    _STRING_1,
    _MULTILINE_1,
    _MULTILINE_2,
    _LIST_1,
    _LIST_2,
    _FLOAT_2,
    _FLOAT_1,
    _BASIC_CONTAINERS_1,
    _BASIC_CONTAINERS_2,
    _TUPLE_1,
    _TUPLE_2,
)


def test_constants() -> None:
    """Test the constant pairs on not the same"""
    assert _INT_1 != _INT_2
    assert _FLOAT_1 != _FLOAT_2
    assert _STRING_1 != _FLOAT_2
    assert _BASIC_TYPES_1 != _BASIC_TYPES_2
    assert _LIST_1 != _LIST_2
    assert _TUPLE_1 != _TUPLE_2
    assert _SET_1 != _SET_2
    assert _BASIC_CONTAINERS_1 != _BASIC_CONTAINERS_2
    assert _ALL_BASIC_TYPES_1 != _ALL_BASIC_TYPES_2


def test_float(float_1: float, float_2: float) -> None:
    assert float_1 != float_2


def test_float_1(float_1: float) -> None:
    assert float_1 == _FLOAT_1


def test_float_2(float_2: float) -> None:
    assert float_2 == _FLOAT_2


def test_int(int_1: int, int_2: int) -> None:
    assert int_1 != int_2


def test_int_1(int_1: int) -> None:
    assert int_1 == _INT_1


def test_int_2(int_2: int) -> None:
    assert int_2 == _INT_2


def test_string(string_1: str, string_2: str) -> None:
    assert string_1 != string_2


def test_string_1(string_1: str) -> None:
    assert string_1 == _STRING_1


def test_string_2(string_2: str) -> None:
    assert string_2 == _STRING_2


def test_multiline(multiline_1: str, multiline_2: str) -> None:
    assert multiline_1 != multiline_2


def test_multiline_1(multiline_1: str) -> None:
    assert multiline_1 == _MULTILINE_1


def test_multiline_2(multiline_2: str) -> None:
    assert multiline_2 == _MULTILINE_2


def test_basic_types(basic_types_1: _BasicTypes, basic_types_2: _BasicTypes) -> None:
    assert basic_types_1 != basic_types_2


def test_basic_types_1(basic_types_1: _BasicTypes) -> None:
    assert basic_types_1 == _BASIC_TYPES_1


def test_basic_types_2(basic_types_2: _BasicTypes) -> None:
    assert basic_types_2 == _BASIC_TYPES_2


def test_list(list_1: _BasicList, list_2: _BasicList) -> None:
    assert list_1 != list_2


def test_list_1(list_1: _BasicList) -> None:
    assert list_1 == _LIST_1


def test_list_2(list_2: _BasicList) -> None:
    assert list_2 == _LIST_2


def test_set(set_1: _BasicSet, set_2: _BasicSet) -> None:
    assert set_1 != set_2


def test_set_1(set_1: _BasicSet) -> None:
    assert set_1 == _SET_1


def test_set_2(set_2: _BasicSet) -> None:
    assert set_2 == _SET_2


def test_tuple(tuple_1: _BasicTuple, tuple_2: _BasicTuple) -> None:
    assert tuple_1 != tuple_2


def test_tuple_1(tuple_1: _BasicTuple) -> None:
    assert tuple_1 == _TUPLE_1


def test_tuple_2(tuple_2: _BasicTuple) -> None:
    assert tuple_2 == _TUPLE_2


def test_basic_containers(
    basic_containers_1: _BasicContainers, basic_containers_2: _BasicContainers
) -> None:
    assert basic_containers_1 != basic_containers_2


def test_basic_containers_1(basic_containers_1: _BasicContainers) -> None:
    assert basic_containers_1 == _BASIC_CONTAINERS_1


def test_basic_containers_2(basic_containers_2: _BasicContainers) -> None:
    assert basic_containers_2 == _BASIC_CONTAINERS_2


def test_all_basic_types(
    all_basic_types_1: _AllBasicTypes, all_basic_types_2: _AllBasicTypes
) -> None:
    assert all_basic_types_1 != all_basic_types_2


def test_all_basic_types_1(all_basic_types_1: _AllBasicTypes) -> None:
    assert all_basic_types_1 == _ALL_BASIC_TYPES_1


def test_all_basic_types_2(all_basic_types_2: _AllBasicTypes) -> None:
    assert all_basic_types_2 == _ALL_BASIC_TYPES_2


def test_parametrized_basic_types_1(parametrized_basic_types_1):
    assert parametrized_basic_types_1 in _LIST_1


def test_parametrized_basic_types_2(parametrized_basic_types_2):
    assert parametrized_basic_types_2 in _LIST_2


def test_parametrized_basic_containers_1(parametrized_basic_containers_1):
    assert (
        _BASIC_CONTAINERS_1[type(parametrized_basic_containers_1)]
        == parametrized_basic_containers_1
    )


def test_parametrized_basic_containers_2(parametrized_basic_containers_2):
    assert (
        _BASIC_CONTAINERS_2[type(parametrized_basic_containers_2)]
        == parametrized_basic_containers_2
    )


def test_parametrized_all_basic_types_1(parametrized_all_basic_types_1):
    assert (
        _ALL_BASIC_TYPES_1[type(parametrized_all_basic_types_1)]
        == parametrized_all_basic_types_1
    )


def test_parametrized_all_basic_types_2(parametrized_all_basic_types_2):
    assert (
        _ALL_BASIC_TYPES_2[type(parametrized_all_basic_types_2)]
        == parametrized_all_basic_types_2
    )
