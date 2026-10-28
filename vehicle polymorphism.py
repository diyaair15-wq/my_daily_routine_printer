class BMW:
    def fuel_type(self):
        return "BMW uses Petrol or Electric."

    def max_speed(self):
        return "BMW max speed is 250 km/h."


class Ferrari:
    def fuel_type(self):
        return "Ferrari uses Premium Petrol."

    def max_speed(self):
        return "Ferrari max speed is 340 km/h."


cars = [BMW(), Ferrari()]

for car in cars:
    print(car.fuel_type())
    print(car.max_speed())
