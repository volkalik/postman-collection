import tempfile

def create_file():
    content = "Hello, this is a test file!"
    temp_file_path = tempfile.mkstemp
    with open(temp_file_path, mode='w') as file:
        file.write(content)
    return temp_file_path

