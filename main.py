# Use for, .split(), and if to create a Statement that will print out words that start with 's':
st = 'Print only the words that start with s in this sentence'


for x in st.split():
    if x[0] == 's':
        print(x)
print('\n')

# Use range() to print all the even numbers from 0 to 10.
list(range(0,11,2))
print(list(range(0,11,2)))
print('\n')

# Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.

li = [l for l in range(1, 51) if l % 3 == 0]
print(li)

# Go through the string below and if the length of a word is even print "even!"
st = 'Print every word in this sentence that has an even number of letters'
s = st.split()
for x in s:
    if len(x)%2 == 0:
        print(x + ' - even')
print('\n')

print('Write a program that prints the integers from 1 to 100.'.upper())
# Write a program that prints the integers from 1 to 100.
# But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".

for x in (range(1,101)):
    if x % 3 == 0 and x % 5 == 0:
        print('- FizzBuzz')
    elif x % 3 == 0:
        print('- Fizz')
    elif x % 5 == 0:
        print('- Buzz')
    else:
        print(x)

print('\n')

# Use List Comprehension to create a list of the first letters of every word in the string below:

print('Use List Comprehension to create a list of the first letters of every word in the string below'.upper())
st = 'Create a list of the first letters of every word in this string'

newlist = [n[0] for n in st.split()]
print(newlist)

mylist = [1,2,3,4]
mylist.append(5)
print(mylist)

mylist.pop()
print(mylist)
help(mylist.insert)


