import pytest
import functools

@functools.lru_cache
def factorial(n):
    assert isinstance(n, int) and n >= 0, f"{n=} must be an integer that is atleast 0"
    if n == 1 or n == 0:
        return 1
    return  n * factorial(n-1)

@functools.lru_cache
def fibonacci(n):
    assert isinstance(n, int) and n >= 0, f"{n=} must be an integer that is atleast 0"
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

def test_factorial():
    assert factorial(5) == 120

def test_fibonacci():
    assert fibonacci(9) == 34
