city_name = input("Enter the city name: ")
temperature = float(input("Enter the temperature in Celsius: "))

if temperature > 35:
    print(f"The weather in {city_name} is extremely hot at {temperature}°C.")
elif temperature > 25:
    print(f"The weather in {city_name} is hot at {temperature}°C.")
elif temperature > 15:
    print(f"The weather in {city_name} is warm at {temperature}°C.")
else:
    print(f"The weather in {city_name} is cold at {temperature}°C.")
import datetime
date = datetime.datetime.now()
