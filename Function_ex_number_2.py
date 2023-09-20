# LESSER OF TWO EVENS
import math

print('LESSER OF TWO EVENS')


def lesser_of_two_evens(a, b, c=10):
    if a % 2 == 0 and b % 2 == 0:
        return min(a, b, c)
    else:
        return max(a, b, c)


r = lesser_of_two_evens(2, 4, 8)
o = lesser_of_two_evens(2, 5, 4)
print(r)
print(o)
print('\n')

print('ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter')


def animal_crackers(text):
    x = text.split()
    if x[0][0] == x[1][0]:
        return True
    else:
        return False


x = animal_crackers('Levelheaded Llama')
v = animal_crackers('Crazy Kangaroo')
print(x)
print(v)
print('\n')

print(
    'MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False')


def makes_twenty(a, b):
    if a + b == 20 or a == 20 or b == 20:
        return True
    else:
        return False


print(makes_twenty(20, 10))
print(makes_twenty(12, 8))
print(makes_twenty(2, 3))
print('\n')

print('''LEVEL 1 PROBLEMS
OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name''')


def old_macdonald(name):
    first_half = name[:3]
    second_half = name[3:]
    return first_half.capitalize() + second_half.capitalize()

print(old_macdonald('macdonald'))
print('\n')

print("MASTER YODA: Given a sentence, return a sentence with the words reversed"
      "master_yoda('I am home') --> 'home am I'"
      "master_yoda('We are ready') --> 'ready are We'")


def master_yoda(text):
    for l in text:
        l = text.split()
        rev_word_l = l[::-1]
    return " ".join(rev_word_l)

print(master_yoda('I am home'))
print(master_yoda('We are ready'))

print('\n')

print('ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200')


def almost_there(n):
    return (abs(100-n) <= 10) or (abs(200-n) <= 10)
print(almost_there(90))
print(almost_there(104))
print(almost_there(150))
print(almost_there(200))
print('\n')

print('''LEVEL 2 PROBLEMS
FIND 33:
Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.''')

def has_33(nums):
    for i in range(0,len(nums)-1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False
print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([ 3, 1, 3,3,3]))
print('\n')

print('''PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
''')
def paper_doll(text):
    result = ''
    for n in text:
        result += n*3
    return result

print(paper_doll('Hello'))
print(paper_doll('Mississippi'))
print('\n')

print('''BLACKJACK: Given three integers between 1 and 11, 
if their sum is less than or equal to 21, return their sum. 
If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, 
if the sum (even after adjustment) exceeds 21, return 'BUST'
''')

def blackjack(a,b,c):
    if sum([a,b,c]) <= 21:
        return sum([a,b,c])
  #  elif 11 in [a,b,c] and sum([a,b,c]):

print('first sum = ', blackjack(5,6,7))
print('\n')

print('''SUMMER OF '69: Return the sum of the numbers in the array, 
except ignore sections of numbers starting with a 6 
and extending to the next 9 (every 6 will be followed by at least one 9). 
Return 0 for no numbers.
''')
def summer_69(arr):
    for n in arr:
        return sum([])


