from basic_2 import one

print('TOP LEVEL IN TWO.PY')

one.func()

if __name__ == '__main__':
    print('TWO.PY is being run directly')
else:
    print('ONE.PY has been imported')