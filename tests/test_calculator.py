import pytest

from calculator import simple_calculator


@pytest.mark.parametrize("num_1, num_2, operation, expected_result", [(3, 3, "+", 6),
                                                                      (3, 5, "*", 15),
                                                                      (3, 3, "/", 1),
                                                                      (3, 3, "-", 0)])
def test_calc(num_1, num_2, operation, expected_result):
    assert simple_calculator(num_1, num_2, operation) == expected_result
# def test_plus():
#     res = simple_calculator("num_1","num_2", "+", )
#     assert res == 6
#
# def test_minus():
#     res = simple_calculator(3,3, "-")
#     assert res == 0
