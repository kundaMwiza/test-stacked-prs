import pytest
import numpy as np

@pytest.fixture
def input_a() -> np.ndarray:
    return np.random.randn(5, 10) 

@pytest.fixture
def input_b() -> np.ndarray:
    return np.random.randn(5, 10)

def test_add(input_a, input_b) -> None:
    result = input_a + input_b
    assert (result != 0 ).all()
