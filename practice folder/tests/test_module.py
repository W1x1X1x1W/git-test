import pytest
from practice_testing import add,divide

def test_add():
    reslt = add(num1=1, num2=3)
    assert reslt == 4

def test_divide():
    reslt = divide(num1=2, num2=2)
    assert reslt == 1