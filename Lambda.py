"Lambda expressions, Map, Filter functions" 
# Task1 
def square(num):
    return num**2
my_nums = [1,2,3,4,5]

for item in map(square,my_nums):
    print(item)

l = list(map(square,my_nums))
print(l)
print('\n')

def splicer(mystring):
    if len(mystring)%2 == 0:
        return 'EVEN'
    else:
        return mystring[0]

names = ['ANdy', 'Eve', 'Sally']
lsp = list(map(splicer,names))
print(lsp)
print('\n')
def check_even(num):
    return num%2 == 0
mynums = [1,2,3,4,5,6]

evl = list(filter(check_even,mynums))
print(evl)

for n in filter(check_even,mynums):
    print(n)
print('\n')

def square(num):
    return num ** 2
print(square(3))

square = lambda num: num ** 2
print(square(4))
print('\n')

def test(a,b):
    return a+b
yv = test(4,8)
print(yv)

print('\n')

# GLOBAL
name = 'This is a global string'
def greet():
    #ENCLOSING
    name = 'Sammy'

    def hello():
        # LOCAL
        name = 'I am a local'
        print('Hello ' +name)

    hello()
print(greet())
print('\n')

x = 50
def func(x):
    print(f'X is {x}')

    # local reassignment
    x = 35
    print('Changed local x to', x)
print(func(20))
print('\n')

x = 50
def func():
    global x
    print(f'X is {x}')


    # local reassignment on a global variable
    x = 'NEW VALUE'
    print(f'I locally Changed GLOBAL x to {x}')
print(x)
print(func())
print(x)

def vol(rad):
    import math
    return (4/3)*math.pi*rad**3

v = vol(2)
print(v)