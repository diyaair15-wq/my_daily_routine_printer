class Person:
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number

    def display(self):
        print(f"Name: {self.name}")
        print(f"ID Number: {self.id_number}")

class Employee(Person):
    def __init__(self, name, id_number, salary, post):
        super().__init__(name, id_number)
        self.salary = salary
        self.post = post

emp = Employee("snow kitten", "EMP1024", 75000, "deisign engineer")
emp.display()
