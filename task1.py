def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def celsius_to_kelvin(celsius):
    return celsius + 273.15


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5 / 9 + 273.15


def kelvin_to_celsius(kelvin):
    return kelvin - 273.15


def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9 / 5 + 32


def convert_temperature(value, from_scale, to_scale):
    from_scale = from_scale.lower()
    to_scale = to_scale.lower()

    if from_scale == "celsius":
        if to_scale == "fahrenheit":
            return celsius_to_fahrenheit(value)
        elif to_scale == "kelvin":
            return celsius_to_kelvin(value)
    elif from_scale == "fahrenheit":
        if to_scale == "celsius":
            return fahrenheit_to_celsius(value)
        elif to_scale == "kelvin":
            return fahrenheit_to_kelvin(value)
    elif from_scale == "kelvin":
        if to_scale == "celsius":
            return kelvin_to_celsius(value)
        elif to_scale == "fahrenheit":
            return kelvin_to_fahrenheit(value)

    return None  # If invalid conversion


# User input
value = float(input("Enter the temperature value: "))
from_scale = input("Enter the scale you're converting from (Celsius, Fahrenheit, Kelvin): ")
to_scale = input("Enter the scale you're converting to (Celsius, Fahrenheit, Kelvin): ")

# Conversion
result = convert_temperature(value, from_scale, to_scale)

if result is not None:
    print(f"{value} {from_scale.capitalize()} is equal to {result:.2f} {to_scale.capitalize()}.")
else:
    print("Invalid conversion.")