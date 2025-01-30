class employee():

    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def display_info(self):
        return f"Name: {self.name}"
        return f"Position: {self.position}"
        return f"Salary: {self.salary}"


employee1 = employee('Doveryun', "QA", 3000)
employee2 = employee('Security', "SB", '4000')
employee3 = employee('Pyatochkin', "BA", '5000')


print(employee1.display_info())
