import pytest
from series import fibonacci

def test_series_zero():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected