# "Warm up"
def lesser_of_two_evens(a,b):
    if a % 2 == 0 and b % 2 == 0:
        return min(a,b)
    else:
        return max(a,b)
l = lesser_of_two_evens(2,4)
print(l)
l = lesser_of_two_evens(6,5)

print(l)
print('\n')

# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
# animal_crackers('Levelheaded Llama') --> True
# animal_crackers('Crazy Kangaroo') --> False

def animal_crackers(text):
    wlist = text.split()
    return wlist[0][0] == wlist[2][0]

print(animal_crackers('Levelheaded Llama lazy Spisok'))
# print(wlist[0])
print(animal_crackers('Crazy Kangaroo Health Gigi'))
print('\n')

# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20.
# If not, return False
print('MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. '
      'If not, return False')
# makes_twenty(20,10) --> True
# makes_twenty(12,8) --> True
# makes_twenty(2,3) --> False

def makes_twenty(n1,n2):
    return n1+n2 == 20 or n1==20 or n2==20
print(makes_twenty(20,10))
print(makes_twenty(12,8))
print(makes_twenty(2,3))
print('\n')

# LEVEL 1 PROBLEMS
# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
print('''LEVEL 1 PROBLEMS
OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name''')

def old_macdonald(name):
    glob = name.split()
    return glob[0].upper()[3].upper()
print(old_macdonald('macdonald'))


def myfunc(*args):
    for x in args:
        print(x)
myfunc(3)
print('\n')


def myfunc(x):
    out = "12345678"
    for i in range(len(x)):
        if i%2==0:
            out.append(x[i].lower())
        else:
            out.append(x[i].upper())
    return ''.join(out)
    print(out)

with open('Function_ex_number_2.py', mode='w') as for_loops:
    for_loops.write("st = 'Print only the words that start with s in this sentence'")
    for_loops.close()
print(for_loops)