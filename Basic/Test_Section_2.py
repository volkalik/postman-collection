import math

x = 100+0.25
print(x)

y = 401/4
print(y)

d = 3**3
print(d)

a = 4*(6+5)
b = 4*6+5
c = 4+6*5
print(a)
print(b)
print(c)

f = 3+1.5+4
print(f, type(f))

g = math.sqrt(9)
e = math.sqrt(121)
r = math.sqrt(16)
print(g, e, r )

u = math.pow(5,3)
print(u, '\n')

print('STRINGS', '\n')

s = 'hello'
print(s[1])
print(s[1:2])
print(s[::-1], '\n')

print(s[4])
print(s[-1], '\n')

# LISTS
print('LISTS', '\n')

l = [0,0,0]
l2 = list((0,0,0))
print(l, '\n', '\n')

list3 = [1,2,[3,4,'hello']]
list3[2][2] = 'goodbye'
print(list3, '\n')

list4 = [5,3,4,6,1]
list4.sort()
print(list4, '\n')

# DICTIONARIES
print('DICTIONARIES', '\n')

d = {'simple_key':'hello'}
print(d['simple_key'])
d = {'k1':{'k2':'hello'}}
print(d['k1']['k2'])
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d['k1'][0]['nest_key'][1][0], '\n')

print('Homework', '\n')

# task_1
print('task_1')
s1 = "Black cat"
s2 = " and 2 Red cats"
print(s1, '\n')

# task_2
print("task_2")
s1 = s1 + s2
print(s1, '\n')

# task_3
print('task_3')
# removing and replacement "2" to "3"
print(s1[14])
s1 = s1[:14] + s1[15:]
s1 = s1[:14] + '3' + s1[14:]
print(s1, '\n')

# task_4
print('task_4')
t5 = ['a','b',0,0,1,2,3,4,4,6,7]
print('list is: ', t5)
print('first element is: ', t5[0])
print('last element is: ', t5[-1])

# task_5
print('task_5')
ryadok = 'QWERTABCDASDF'
print('ryadok  is: ', ryadok)
new_ryadok= ryadok.replace('A','Z')
print(new_ryadok)

print('')
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(d['k1'][2]['k2'][1]['tough'][2][0])

if 3 > 4:
    print("happy")
elif 1 > 2:
    print("sad")
else:
    print('NV')
