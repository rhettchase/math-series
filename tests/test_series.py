import pytest
from series.series import fibonacci, lucas, sum_series

def test_fib_zero():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected
    
def test_fib_one():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected
    
def test_fib_5():
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

def test_sum_series_0():
    actual = sum_series(0)
    expected = 0
    assert actual == expected
    
def test_sum_series_5():
    actual = sum_series(5,2,1)
    expected = 11
    assert actual == expected

def test_sum_series_1():
    actual = sum_series(1)
    expected = 1
    assert actual == expected
    
def test_sum_series_701():
    actual = sum_series(7,0,1)
    expected = 13
    assert actual == expected

def test_sum_series_3_10_10():
    actual = sum_series(3,10,10)
    expected = 30
    assert actual == expected

def test_sum_series_5_4_7():
    actual = sum_series(5, 4, 7)
    expected = 47
    assert actual == expected