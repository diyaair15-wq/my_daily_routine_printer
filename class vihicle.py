class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

class Car(Vehicle):
    pass

model_s = Car(250, 18)

print("Car Max Speed:", model_s.max_speed)
print("Car Mileage:", model_s.mileage)
