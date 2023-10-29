# test_calculator.py

import pytest
from Calculator.Calc_module import Calculator
from contextlib import nullcontext as does_not_raise

class TestCalculator:

    @pytest.fixture
    def calculator(self):
        return Calculator()  # фикстура, предоставляющая экземпляр калькулятора


@pytest.mark.parametrize("x,y,exp_result", [(2, 3, 5),
                                            (4, 5, 9),
                                            (12, 10, 22)
                                            ])
def test_addition(x, y, exp_result):
    calcul_spec = Calculator()
    result = calcul_spec.add(x, y)
    assert result == exp_result


@pytest.mark.parametrize("x,y,exp_result", [(2, 3, -1),
                                            (5, 5, 0),
                                            (-4, 4, -8),
                                            (-6, -6, 0),
                                            (7, 6, 1)
                                            ])
def test_subtraction(x,y, exp_result):
    calcul_spec = Calculator()
    result = calcul_spec.subtract(x,y)
    assert result == exp_result

@pytest.mark.parametrize("x,y,exp_result", [(2, -3, -6),
                                            (3,3,9)
                                            ])

def test_multiplication(x,y, exp_result):
    calcul_spec = Calculator()
    result = calcul_spec.multiply(x,y)
    assert result == exp_result

@pytest.mark.parametrize("x,y,exp_result,expect", [(2, 2, 1, does_not_raise()),
                                            (3,-3,-1, does_not_raise()),
                                            (3,0,0, pytest.raises(ValueError))
                                            ])
def test_division(x,y,exp_result, expect):
    with expect:
        calcul_spec = Calculator()
        result = calcul_spec.divide(x,y)
        assert result == exp_result
#    with pytest.raises(ZeroDivisionError):
#       assert result == ZeroDivisionError

