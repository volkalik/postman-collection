def hello(name='Jose'):
    print("The hello() function has been executed")

    def greet():
        return "\t This is the greet() func inside hello"

    #    print(greet())

    def welcome():
        return "\t This is the welcome() func inside hello"

    #    print(welcome())
    print('This is the end of the hello function')

    if name == 'Jose':
        return greet
    else:
        return welcome


my_new_func = hello('Jose')
print(my_new_func())


def cool():
    def super_cool():
        return "I am very cool!\n"

    return super_cool()


some_func = cool()
print(some_func)


def hello():
    return 'Hi Jose!\n'

def other(some_def_func):
    print('Other code runs here')
    print(some_def_func)

other(hello())


def new_decorator(original_func):

    def wrap_func():
        print('Some extra code, BEFORE the original function')

        original_func()

        print('Some extra code, AFTER the original function')

    return wrap_func()

@new_decorator
def func_needs_decorator():
    print('I want to be decorated!')


def inc():
    pass