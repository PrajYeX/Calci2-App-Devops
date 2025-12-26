# tests/test_core.py
import pytest
from calculator.core import add, sub, mul

def test_add_basic():
    assert add(2, 3) == 5
    assert add(0, 0) == 0

def test_sub_basic():
    assert sub(5, 3) == 2
    assert sub(0, 0) == 0

def test_mul_basic():
    assert mul(4, 3) == 12
    assert mul(0, 5) == 0

@pytest.mark.parametrize("a,b", [(1, -1), (-2, 3)])
def test_negative_inputs_raise(a, b):
    with pytest.raises(ValueError):
        add(a, b)  # any function validates, so expect ValueError or TypeError

def test_type_error_on_non_int():
    with pytest.raises(TypeError):
        add(2.0, 3)
