def say_hello(name):
    print(f'Hello {name}')


say_hello('Alik')
print('\n')


def myfunc(a, b):
    return a + b


result = myfunc(5, 10)
print(result)

x = 21 % 2 == 0
print(x)


def even_check(number):
    r = number % 2 == 0
    return r


print(even_check(200))
print('\n')


def check_even_list(num_list):
    even_numbers = []
    for number in num_list:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            pass
    return even_numbers


print(check_even_list([1, 3, 2, 5, 8]))
print('\n')

stock_prices = [('AAPL', 200), ('GOOG', 300), ('MSFT', 400)]
for item in stock_prices:
    print(item)
for a, b in stock_prices:
    print(a)
print('\n')

work_hours = [('Abby', 100), ('Billy', 4040), ('Cassie', 800)]


def employee_check(work_hours):
    current_max = 0
    employee_of_month = ''

    for employee, hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass

    return employee_of_month, current_max


result = (employee_check(work_hours))

print(result)
print('\n')

example = [1, 2, 3, 4, 5, 6, 7]
from random import shuffle

shuffle(example)
print(example)
print('\n')


def shuffle_list(mylist):
    shuffle(mylist)
    return mylist


result = shuffle_list(example)
print(result)

mylist = [' ', 'O', ' ']
shuffle_list(mylist)
print(mylist)


def player_guess():
    guess = ''

    while guess not in ['0', '1', '2']:
        guess = input("pick a number: 0,1, or 2: ")

        return int(guess)


myindex = player_guess()
print('myindex is: ', myindex)


def check_guess(mylist,guess):
    if mylist[guess] == 'O':
        print('Correct Guess!')
    else:
        print('Wrong! Better luck next time')
        print(mylist)


mylist = [' ', 'O', ' ']

mixedup_list = shuffle_list(mylist)

guess = player_guess()

check_guess(mixedup_list,guess)

with open('test_6.py', mode='w') as test_6:
    test_6.write("# Function exercises".upper())
    test_6.close()
