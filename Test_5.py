# Task_1
print('Task_1'.upper())
st = 'Print only the words that start with s in this sentence'

for x in st.split():
    if x.startswith('s'):
        print(x)
print('\n')

# Task_2
print('Task_2'.upper())
mylist = range(0,11,2)
for y in mylist:
    print(y)
print('\n')

# Task_3
print('Task_3'.upper())
# Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
l3 = list(range(1,51))
for l in l3:
    if l%3 == 0:
        print(l)

print('\n')

# Task_4
print('Task_4'.upper())
# Go through the string below and if the length of a word is even print "even!"
st = 'Print every word in this sentence that has an even number of letters'
for x in st.split():
    if len(x)%2 == 0:
        print(x+ ' is even')
#    else:
#        print(x+ ' is not even')

print('\n')

# Task_5
print('Task_5'.upper())
# Write a program that prints the integers from 1 to 100.
# But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".

l5 = range(1,100)
for x in l5:
    if x%3 == 0:
        print(x, '= Fizz')
for x in l5:
    if x%5 == 0:
        print(x, "= Buzz")
for x in l5:
    if x%3 ==0 and x%5 == 0:
        print(x, "= BuzzFizz")

print('\n')

# Task_6
print('Task_6'.upper())
# Use List Comprehension to create a list of the first letters of every word in the string below:
st = 'Create a list of the first letters of every word in this string'

st = [r[0] for r in st.split()]
print(st)

print('\n')

# Task_5
print('Task_5'.upper())
# Write a program that prints the integers from 1 to 100.
# But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".
l5 = range(0,101)
for x in l5:
    if x%3 == 0 and x%5 == 0:
        print('Buzzfizz')
    elif x%5 == 0:
        print('Buzz')
    elif x%3 == 0:
        print('Fizz')
    else:
        print(x)

print('\n')

with open('Lambda.py', mode='w') as s6:
    print(s6.write('"Lambda expressions, Map, Filter functions" \n# Task1 \n'))
    s6.close()
