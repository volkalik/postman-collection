class Sample():
    pass


my_sample = Sample()
print(type(my_sample))


class Dog():
    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

    def bark(self, number):
        print("WOOF! My name is {} and number is {}".format(self.name, number))

my_dog = Dog(breed='lab', name='Deny')


#print(type(my_dog), '\n')

#print(my_dog.breed, my_dog.name)

print(my_dog.bark(7), '\n')

class Circle():

    pi = 3.14
    def __init__(self, radius=1):
        self.radius = radius

    def get_circumference(self):
        return self.radius * self.pi * 2

my_circle = Circle(30)
print(my_circle.pi)
print(my_circle.radius)
print(my_circle.get_circumference(), '\n')

class Animal():
    def __init__(self):
        print("Animal Created")

    def who_am_I(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")

myanimal = Animal()
print(myanimal.eat(), '\n___________________________\n')

cla
