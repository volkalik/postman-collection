def read_from_file(filepath):
    with open(filepath, "r") as f_o:
        return f_o.readlines()

print(read_from_file("my_funcs/prodfile.txt"))