def func_decorator(func):
    def wrapper():
        print("--- something before function ---")
        func()
        print("--- something after function ---")

    return wrapper

def some_func():
    print("вызов функции some_func")

f = func_decorator(some_func)
f()

print("\n--------------\n")

def func_decorator(func):
    def wrapper():
        print("--- something before function ---")
        func()
        print("--- something after function ---")

    return wrapper

def some_func():
    print("вызов функции some_func")

f = func_decorator(some_func)
f()
