
# User input

unit = input("Is the temperature in Celsius or Fahrenheit?: ")
temperature = float(input("What is the current temperature?: "))

# Converts celsius to fahrenheit and vice-versa

if unit == "Celsius":
    print(f" The temperature in Fahrenheit is {round((temperature * (9/5)) + 32, 1)}")

elif unit == "Fahrenheit":
    print(f"The temperature in Celsius is {round((temperature - 32) * (5/9), 1)}")

else:
    print(f"{unit} is not a valid unit!")