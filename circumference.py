import math


def calculate_circumference(radius):
    return 2.0 * math.pi * radius


r=input("pls enter a radius:  ")
print("circumference = ",calculate_circumference(float(r)))

