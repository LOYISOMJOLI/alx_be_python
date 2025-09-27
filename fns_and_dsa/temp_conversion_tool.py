FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9

CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return fahrenheit * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR

temp = float(input("Enter the temperature to convert:"))
f_or_c = input("Is this temperature in Celsius or Fahrenheit? (C/F):")

if f_or_c == "C":
    print(f"{temp} C is {convert_to_fahrenheit(temp)} F")

if f_or_c == "F":
    print(f"{temp} F is {convert_to_celsius(temp)} C")


