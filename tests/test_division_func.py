from my_funcs.utils import division
import pytest


@pytest.mark.parametrize("a, b ,expected_result", [(10, 2, 5),
                                                   (10, 5, 2),
                                                   (20, -2, -10),
                                                   (5, 2, 2.5)])
def test_division_good(a, b, expected_result):
    assert division(a, b) == expected_result

@pytest.mark.parametrize("expected_exception, divider, divisionable",
                         [(ZeroDivisionError, 0, 10),
                          (TypeError, "2", 20)])
def test_zero_division_with_error(expected_exception, divider, divisionable):
     with pytest.raises(expected_exception):
         division(divisionable, divider)

