[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![License: MIT](https://img.shields.io/badge/License-MIT-blueviolet.svg)](https://opensource.org/licenses/MIT)

# pytest-builtin-types

pytest-builtin-types gives you prebuilt builtin data types for testing your own projects.

## Key Features:
* **Basic Types**: Has a selection of fixtures with pre-built types such as `float`, `int`, `str`, etc.
* **Basic Containers**: Has a selection of fixtures with pre-built containers such as `dict`, `list`, `tuple` etc.
* **Great Developer Experience**: Being fully typed makes it great for editor support.

## Installation
`pip install pytest-builtin-types`

## Example

### Basic Type
```python
def test_float_type(float_1, float_2):
    print(float_1) # 1.1
    print(float_2) # 2.1
```
### Basic Types
```python
def test_basic_types(basic_types_1, basic_types_2):
    print(basic_types_1) # {<class 'str'>: 'string1', <class 'int'>: 1, <class 'float'>: 1.1}
    print(basic_types_2) # {<class 'str'>: 'string2', <class 'int'>: 2, <class 'float'>: 1.2}
```
### Basic Containers
```python
def test_container_types(basic_containers_1):
    print(basic_containers_1) 
    # {<class 'list'>: ['string1', 1, 1.1], <class 'tuple'>: ('string1', 1, 1.1), <class 'set'>: {1, 'string1', 1.1},
    # <class 'dict'>: {<class 'str'>: 'string1', <class 'int'>: 1, <class 'float'>: 1.1}}
```