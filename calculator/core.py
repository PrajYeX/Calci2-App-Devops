# calculator/core.py


def _validate_positive_integer(x, name="value"):
    if not isinstance(x, int):
        raise TypeError(f"{name} must be int, got {type(x).__name__}")
    if x < 0:
        raise ValueError(f"{name} must be non-negative (got {x})")

def add(a: int, b: int) -> int:
    _validate_positive_integer(a, "a")
    _validate_positive_integer(b, "b")
    return a + b

def sub(a: int, b: int) -> int:
    _validate_positive_integer(a, "a")
    _validate_positive_integer(b, "b")
    return a - b

def mul(a: int, b: int) -> int:
    _validate_positive_integer(a, "a")
    _validate_positive_integer(b, "b")
    return a * b
