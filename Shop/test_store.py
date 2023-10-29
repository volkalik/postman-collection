import pytest
from Shop.Store import Product


@pytest.fixture()
def create_product():
    def _create_product(name, color, price, quantity):
        return Product(name, color, price, quantity)

    return _create_product


@pytest.mark.parametrize("name, color, price, quantity, exp_cost", [
    ("phone", "yellow", 5500, 3, 16500),
    ("toy", "red", 1000, 4, 4000)
])
def test_product_cost(create_product, name, color, price, quantity, exp_cost):
    product = create_product(name, color, price, quantity)
    if product.color == 'yellow':
        assert product.total_cost() == exp_cost
    else:
        assert product.total_cost() == exp_cost
