class Bird:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

    def fly(self):
        print(f"{self.name} is flying.")

class Penguin(Bird):
    def __init__(self, name, speed):
        super().__init__(name)
        self.speed = speed

    def swim(self):
        print(f"{self.name} swims at {self.speed} mph.")

    def info(self):
        print(f"This is a {self.name}.")

p = Penguin("Penguin", 12)
p.eat()
p.fly()
p.swim()
p.info()
