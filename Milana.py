def say_hello(name):
    print(f"hello {name}")
say_hello('Doverun')

def add_num(n1,n2):
    return n1+n2
result = add_num(10,20)

def print_result(a,b):
    print(a+b)
print_result(15,24)

# Logic with python functions
def even_check(number):
    return number % 2 == 0
print(even_check(20))
print('\n')


# return true if any number is even inside a list
def check_even_list(num_list):

    even_numbers = []
    for number in num_list:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            pass
    return even_numbers
print(check_even_list([1,2,3,4,5,6,8,9,9,14]))

# Tuples unpacking

stock_prices = [('appl', 200), ('goog', 300), ('xiaom', 100)]
for item in stock_prices:
    print(item)
print('\n')

for a,b in stock_prices:
    print(b+(0.1*b))
print('\n')


work_hours = [('Abby',100),('Billy',5400),('Cassie',800)]


def employee_check(work_hours):
    # Set some max value to initially beat, like zero hours
    current_max = 0
    # Set some empty value before the loop
    employee_of_month = ''

    for employee, hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass

    # Notice the indentation here
    return (employee_of_month, current_max)
result = employee_check(work_hours)
print(result)
print('\n')

example = [1,2,3,4,5,6,7]
from random import shuffle
shuffle(example)
print(example)

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist
result = shuffle_list(example)
print(result)
print('\n')

mylist = ['','O','']
print(shuffle_list(mylist))
print('\n')

def player_guess():
    guess = ''
    while guess not in ['1','2','3']:
        guess = input('pick a number: 0,1, or 2 ')
    return int(guess)
# player_guess()
# print(player_guess())

myindex = player_guess()
# print('myindex is ', myindex)


def check_guess(mylist,guess):
    if mylist[guess] == '0':
        print('Correct!!!')
    else:
        print('Wrong guess!')
        print(mylist)
# Initial List
mylist = [' ','O',' ']

# Shuffle It
mixedup_list = shuffle_list(mylist)

# Get User's Guess
guess = player_guess()

# Check User's Guess
check_guess(mixedup_list,guess)

# Notice how this function takes in the input
# based on the output of other functions!

