import pytest
from Person.person import Person, get_person_info


@pytest.fixture
def person_info():
    return Person(name='Udivlun',
                  age=8
                  )


def test_person(person_info):
    result = get_person_info(person_info)
    exp_res = "Udivlun is 8 years old"
    assert result == exp_res


