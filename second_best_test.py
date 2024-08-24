import pytest
import functools

@functools.lru_cache
def factorial(n):
    if n == 1 or n == 0:
        return 1
    return  n * factorial(n-1)

def test_factorial():
    assert factorial(5) == 120

