from app.calculator import add, safe_divide
import pytest

def test_add_incorrect_on_purpose():
    #Fixed assertion
    assert add(2,3) == 5

def test_safe_divide_zero_error():
    with pytest.raises(ZeroDivisionError):
        safe_divide(1, 0)   