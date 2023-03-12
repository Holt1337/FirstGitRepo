from simple_library_01.functions import is_leap

import pytest


def test_is_leap():
    assert is_leap(2000)

def test_not_is_leap():
    assert not is_leap(2001)

def test_not_is_leap():
    assert not is_leap(2100)

def test_atribute_error():
    with pytest.raises(AttributeError):
        is_leap(-1)
