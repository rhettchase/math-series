import pytest
from series.series import fibonacci, lucas

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

def test_lucas_zero():
    actual = lucas(0)
    expected = 2
    assert actual == expected
    
def test_lucas_one():
    actual = lucas(1)
    expected = 1
    assert actual == expected
    
def test_lucas_5():
    actual = lucas(5)
    expected = 11
    assert actual == expected
    
def test_lucas_7():
    actual = lucas(7)
    expected = 29
    assert actual == expected
    