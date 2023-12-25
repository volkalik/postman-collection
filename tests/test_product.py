import pytest
from basic_2.product import Product


@pytest.fixture()
def store():
    return Product("jeans", 50, 10)


def test_product(store):
    assert store.name == "jeans"
    assert store.price == 50
    assert store.stock == 10


def test_update_price(store):
    store.update_price(65)
    assert store.price == 65


def test_add_stock(store):
    store.add_stock(25)
    assert store.stock == 35


def test_sell(store):
    store.sell(3)
    assert store.stock == 7
