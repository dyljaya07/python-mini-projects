# Python Weight Converter

weight = float(input("Please enter your weight: "))
current_format = input("Please enter your format (K or L): ")

if current_format == "K":
    weight =  weight * 2.205
    print (f"Your weight in Pounds is {weight}lbs!")

elif current_format == "L":
    weight = weight / 2.205
    print (f"Your weight in Kg is {round(weight, 1)}kgs!")

else:
    print("Please enter a valid format")
