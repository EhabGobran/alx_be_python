FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_fahrenheit(celsius):
    fahrenheit = CELSIUS_TO_FAHRENHEIT_FACTOR * celsius + 32
    return fahrenheit

def convert_to_celsius(fahrenheit):
    celsius = FAHRENHEIT_TO_CELSIUS_FACTOR * (fahrenheit - 32)
    return celsius


if __name__ == "__main__":
    temprature = int(input("Enter the temperature to convert: "))

    temprature_type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
    match temprature_type:
        case "C":
            fahrenheit = convert_to_fahrenheit(temprature)
            print(f"{temprature}°C is {fahrenheit}°F")

        case "F":
            celsius = convert_to_celsius(temprature)
            print(f"{temprature}°F is {celsius}°C")
    

    pass