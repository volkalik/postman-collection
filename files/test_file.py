import tempfile
import os
from urllib import request

import pytest

@pytest.fixture()
def create_file():
    content = "Hello, this is a test file!"
    file_fd, temp_file_path = tempfile.mkstemp()
    with open(temp_file_path, 'w') as file:
        file.write(content)

    def remove_file():
        os.remove(temp_file_path)

    request.addfinalizer(remove_file)
    return temp_file_path


def test_file_exists(create_file):
    with open(create_file, 'r') as r_file:
        content = r_file.read()
    assert "test file" in content

def remove_test_file(create_file):
    with open(create_file, 'r') as r_file:
        content = r_file.read()
    assert "test file" not in content
