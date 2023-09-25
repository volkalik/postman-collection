my_list = ['one',2,'three', 'four']

second_list = [5, 'six', 7]
print(my_list + second_list)

new_list = my_list+second_list
print(new_list)

new_list[0] = 'ONE ALL'
print(new_list)
print('\n')
new_list.append('eight')
print(new_list)
new_list.append('ten')
print(new_list)
print('\n')
new_list[8] = 'nine'
print(new_list)
print('\n')

popped_item = new_list.pop(0)
print(popped_item)
print(new_list)
print('\n')

add_list = ['a', 'e', 'x', 'b', 'c']
num_list = [4,1,8,3]

add_list.sort()
print(add_list)

aa = add_list.sort()
print(type(aa))
print('\n')


print(num_list)
num_list.sort()
print(num_list)

num_list.reverse()
print(num_list)
print('\n', '\n')
print("DICTIONARIES")

d = {'k1': 123, 'k2':[0,1,333], 'k3':{'inskey':100}}
print(d['k3']['inskey'])
print(d['k2'][2])
print('\n')

d = {'k1':100, 'k2': 200}
d['k5'] = 500
print(d)

d['k8'] = 420
print(d)

d['k1'] = 'rest'
print(d)
print(d['k1'])

d.keys()
print(d.keys())
print(d.values())
print(d.items())
print('\n \n')

t = (1,2,3)
my_list = [1,2,3]

myfile = open('secondfile.txt')

contents = myfile.read()
print(contents)

newfile = open('firstfile.txt')
frst = newfile.read()
print(frst)
nnw = newfile.readlines()
print(nnw)

myfile = open('/Users/oleksandr.volk/Documents/My/hlab.txt')
print(myfile.read())
myfile.close()

with open('/Users/oleksandr.volk/Documents/My/hlab.txt', mode = 'r') as hfile:
    contet = hfile.read()
print(contet)

with open('/Users/oleksandr.volk/Documents/My/bearfile.txt', mode='w') as nfile:
    nfile.write('\nDoverun believes me \n')

with open('/Users/oleksandr.volk/Documents/My/bearfile.txt', mode= 'r') as rfile:
    print(rfile.read())

with open('/Users/oleksandr.volk/Documents/My/bearfile.txt', mode='a') as rfile:
    rfile.write('Pyatochkin was helping to water plants')

with open('/Users/oleksandr.volk/Documents/My/bearfile.txt', mode= 'r') as rfile:
    print(rfile.read())

with open('/Users/oleksandr.volk/Documents/My/one more file.txt', mode='w') as mf:
    mf.write('Nafig pichalku')

with open('/Users/oleksandr.volk/Documents/My/one more file.txt', mode='r') as mf:
    print(mf.read())

file = open('/Users/oleksandr.volk/Documents/My/thirdfile.txt', 'w')
file.write('hello team')
file.close()

file = open('/Users/oleksandr.volk/Documents/My/thirdfile.txt', 'r')
print(file.read())

s5 = open('Remember.py', 'w')
s5.write("# Home tasks")
s5.close()
with open('Remember.py', mode= 'r') as s5:
    print(s5.read())
s5.close()

