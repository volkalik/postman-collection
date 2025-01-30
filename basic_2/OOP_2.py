class Dog():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says, woof!"

class Cat():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says, meow!"

niko = Dog("niko")
felix = Cat('felix')

print(niko.speak())
print((felix.speak()))
print('\n___________\n')

#for pet in [niko,felix]:
#    print(pet.speak())


#def pet_speak(pet):
#    print(pet.speak(),'\n')



class Animal():
    def __init__(self,name):
        self.name = name

    def speak(self):
        raise NotImplementedError("subclass does not exist")

class Dog(Animal):
    def speak(self):
        return self.name + " says woof!"

class Cat(Animal):
    def speak(self):
        return self.name + " says meow!"

fred = Cat('fred')
Denny = Dog('Denny')

print(fred.speak())
print(Denny.speak())
print('\n___________\n')


mylist = [1,2,3]
(len(mylist))

class Sample():
    pass
mysample = Sample()

print(mysample)
