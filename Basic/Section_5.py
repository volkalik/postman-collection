# PYTHON STATEMENTS
# IF, ELIF, ELSE
print("If, elif, else".upper())
hungry = 0
if hungry:
    print("Feed me!")
else:
    print("I'm not hungry")

loc = 'Bank'

if loc == 'Auto Shop':
    print('Cars are cool!')
else:
    print('I dont know much.', '\n')

name = 'Mat'
if name == 'Sammy':
    print('Hello Sammy!')
elif name == 'Frankie':
    print('Hello Frankie!')
elif name == 'Mat':
    print('Hello Mat!')
else:
    print("What is your name?")
print('\n')

# For loops
print('"for loops"'.upper())

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in mylist:
    print(num)
print('----------', '\n')
for num in mylist:
    if num % 2 == 0:
        print(num)
    else:
        print(f'Odd Number: {num}')
print('\n')

list_sum = 0

for num in mylist:
    list_sum = list_sum + num
print(list_sum, '\n')

mystring = 'Hello World!'
for letter in mystring:
    print(letter)
print('\n')

for _ in 'Happy':
    print('Cool!')
print('\n')

tup = (1,2,3)
for item in tup:
    print(item)
print('\n')

newlist = [(1,2), (3,4), (5,6), (7,8)]
print('length', len(newlist))
for p in newlist:
    print(p)

newlist = [(1,2), (3,4), (5,6), (7,8)]
for (a,b) in newlist:
    print(a)
    print(b)
print('\n')

d = {'k1':1, 'k2':2, 'k3':3}
for item in d.items():
    print(item)

dd = {'k1':1, 'k2':2, 'k3':3}
for key, value in dd:
    print(key, 'is', value)
print('\n')

# While loops
print("while loops".upper())

x = 10
while x < 5:
    print(f'the current of x is {x}')
    x += 1
#   x = x + 1

else:
    print("'x is not les than 5'")
print('\n')

x = [1,2,3]
for item in x:
    # comment
    pass
print('end of my script')
print('\n')

mystring = 'Sammy'
for letter in mystring:
    if letter == 'a':
        continue
    print(letter)
print('\n')

mystring = 'Sammy'
for letter in mystring:
    if letter == 'a':
        break
    print(letter)
print('\n')

x = 0
while x < 5:
    if x == 2:
        break
    print(x)
    x += 1
print('\n')

# useful operators
print("useful operators".upper())

mylist = [1,2,3]
for num in range(0,11,2):
    print(num)

print(range(0,11,2))
print(list(range(0,11,2)))
print('\n')

index_count = 0

for letter in 'abcde':
    print('At index {} the letter is {}'.format(index_count, letter))
    index_count += 1
print('\n')

# another thing
index_count = 0
word = 'abcde'
for letter in word:
    print(word[index_count])
    index_count += 1
print('\n')

word = 'abcde'
for item in enumerate(word):
    print(item)
print('\n')

word = 'abcde'
for index, letter in enumerate(word):
    print(index)
    print(letter)
    print('\n')

mylist1 = [1,2,3]
mylist2 = ['a','b','c']
mylist3 = [100,200,300]

for a,b,c in zip(mylist1,mylist2, mylist3):
    print(b)

list(zip(mylist1, mylist2))
print(list(zip(mylist1, mylist2)))
print('\n')



'mykey' in {'mykey': 345}
print('mykey' in 'mykey')

d = {'mykey': 345}
print(345 in d.values())
print('\n')

mylist = [10, 20, 30, 40, 100]
print(min(mylist))
print(max(mylist))
print('\n')

from random import shuffle
mylist = [1,2,3,4,5,6,7,8,9,10]
shuffle(mylist)
print(mylist)
print('\n')

from random import randint
f = randint(0,100)
print(f)
print('\n')

# input('Enter aa number here: ')
# print(input())

# result = input('What is your name? ')
# print(result)

# result = input('first number: ')
# print(float(result))
# print(type(result))
print('\n')

# test = int(input('Fav number: '))
# print(type(test))
# print('\n')

# LIST COMPREHENSIONS
print("LIST COMPREHENSIONS".lower())

mystring = 'hello'
mylist = []
for letter in mystring:
    mylist.append(letter)
print(mylist)

# way 2
mylist2 = [letter for letter in mystring]
print(mylist2)

mylist3 = [x for x in 'this is new string']
print(mylist3)

mylist4 = [num for num in range(0,11)]
print(mylist4)

mylist5 = [num**2 for num in range(0,12)]
print(mylist5)

mylist6 = [x**2 for x in range(0,11) if x%2==0]
print(mylist6)
print('\n')

celcius = [1,10,20,34.5]
fahrenheit = [((9/5)*temp + 32) for temp in celcius]
print('temperature', fahrenheit)

fahrenheit = []
for temp in celcius:
    fahrenheit.append(((9/5)*temp + 32))
print(fahrenheit)

results = [x if x%2==0 else 'ODD' for x in range(0,11)]
print(results)

print('\n')

mylist7 = []
for x in [2,4,6]:
    for y in [1,10,1000]:
        mylist7.append(x*y)
print(mylist7)
print('\n')

mylist = [x*y for x in [2,4,6] for y in [1,10,1000]]
print(mylist)

# with open('Test_5.py', mode='w') as test_5:
#    test_5.write("st = 'Print only the words that start with s in this sentence'")
# test_5.close()
# print(test_5)