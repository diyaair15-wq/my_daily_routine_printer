class Vehicle:
    def __init__(self, capacity):
        self.capacity = capacity

    def get_fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def get_fare(self):
        return super().get_fare() * 1.10

my_bus = Bus(50)
print(my_bus.get_fare())
