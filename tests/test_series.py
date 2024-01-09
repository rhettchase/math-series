import pytest
from series.series import fibonacci

def test_series_zero():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected
    
def test_series_one():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected
    
def test_series_5():
    actual = fibonacci(5)
    expected = 5