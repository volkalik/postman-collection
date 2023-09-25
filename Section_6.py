def myfunc(*args):
    for item in args:
        print(item)

myfunc(20,30,40)

def myfunc(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print('my fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit')

myfunc(fruit='apple', veggie= 'lettuce')
print('\n')


def myfunc(*args, **kwargs):
    if 'fruit' and 'juice' in kwargs:
        print(f"I like {' and '.join(args)} and my favorite fruit is {kwargs['fruit']}")
        print(f"May I have some {kwargs['juice']} juice?")
    else:
        pass


myfunc('eggs', 'spam', fruit='cherries', juice='orange')
