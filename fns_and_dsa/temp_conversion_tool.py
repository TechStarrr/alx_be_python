FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


temperature = int(input("Enter the temperature to convert :"))
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F) :").strip().lower()


def convert_to_celsius(fahrenheit) :
    return fahrenheit - 32 * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius) :
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32



if temperature == "C" or "celsuis" :
    result = convert_to_celsius(temperature)
    print(result)

elif temperature == "F" or "Farenheit" : 
    result = convert_to_fahrenheit(temperature)
    print(result)

else :
    raise ValueError("Invalid unit. Please enter 'C' or 'F'.")