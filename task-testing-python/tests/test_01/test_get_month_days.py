from simple_library_01.functions import get_month_days

import pytest


@pytest.mark.parametrize(
    ['a', 'b',  'answer'], [
        (1930, 3, 30),
        (2003, 2, 28),
        (2020, 2, 29),
        (2020, 4, 30),
        (2020, 5, 31)
    ])
def test_get_month_days(a, b, answer):
    assert answer == get_month_days(a, b)


def test_atribute_error():
    with pytest.raises(AttributeError):
        get_month_days(2001, -1)
