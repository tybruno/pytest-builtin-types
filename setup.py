"""Setup.py file"""
from setuptools import setup

setup(
    name="pytest-builtin-types",
    version="0.0.1",
    # the following makes a plugin available to pytest
    entry_points={"pytest11": ["builtin-types = pytest_builtin_types"]},
    # custom PyPI classifier for pytest plugins
    classifiers=["Framework :: Pytest"],
)