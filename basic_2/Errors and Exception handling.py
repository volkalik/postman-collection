try:
    f = open('testfile','r')
    f.write('Test write this')
except IOError:
    # This will only check for an IOError exception and then execute this print statement
    print("Error: Could not find file or read data")
else:
    print("Content written successfully")
    f.close()
finally:
    print('final text\n\n',
          '--------------------------------\n'
          'homework\n'.upper(),
          'Task 1')

# TASK 1
test_list = ['a','b','c']
for i in test_list:
    try:
        d = (i**2)
        print(d)
    except TypeError:
        print("it's a string instead of integer")
else:
    test_list = ['2', '3', '4']
    int_i_list = [int(n) for n in test_list]
    d = [x**2 for x in int_i_list]
    print(d, '\n\n Task 2')

# TASK 2
x = 5
y = 0
try:
    z = x/y
    print(z)
except TypeError:
    print('string to letter')
except ZeroDivisionError:
    print('You cannot divide this')
finally:
    print('All done \n\n '
          'Task 3')

#TASK 3
def ask():
    global x
    while True:
        try:
            a = int(input('Enter a number: '))
            x = (a**2)
        except ValueError:
            print('A letter cannot be squared')
        else:
            print(f'yes {a} is an integer')
            break
    print('x =',x)
ask()




