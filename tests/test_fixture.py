import pytest
from basic_2.OOP_1 import Dog


@pytest.fixture
def bears():
    family = ['Odnopup', 'Dobryun', 'Pyatochkkin', 'Doveryun']
    return family


def add_bears(bears):
    new_bears = 'Security'
    bears.append(new_bears)
    assert bears == ['Odnopup', 'Dobryun', 'Pyatochkkin', 'Doveryun', 'Security']

def test_add_bears(bears):
    add_bears(bears)


@pytest.fixture
def some_data():
    return int('50')

def test_some_data(some_data):
    assert some_data == 50

@pytest.fixture
def dog_bark():
    return Dog(breed='york', name='Deny')

def test_dog(dog_bark):
    my_dog = dog_bark
    assert my_dog.bark(7) == 'WOOF! My name is Deny and number is 7'

