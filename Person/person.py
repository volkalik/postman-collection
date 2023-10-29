class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def get_person_info(person):
    return f'{person.name} is {person.age} years old'

