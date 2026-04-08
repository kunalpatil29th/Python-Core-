# unit_converter.py

"""
Project: Unit Converter
Converts between different units like Celsius to Fahrenheit and Kilometers to Miles.
"""

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def km_to_miles(km):
    return km * 0.621371

c = 25
km = 10
print(f"{c}°C is {celsius_to_fahrenheit(c)}°F")
print(f"{km}km is {km_to_miles(km)} miles")
