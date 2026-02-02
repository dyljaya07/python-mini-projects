# Python calculator
# addition, subtraction, multiplication, division

operator = input("Please select an arithmetic operator (+ , -, *, /): ")
number_1 = float(input("Please enter the first number: "))
number_2 = float(input("Please enter the second number: "))

if operator == "+":
    result = number_1 + number_2
    print(result)

elif operator == "-":
    result = number_1 - number_2
    print(result)

elif operator == "*":
    result = number_1 * number_2
    print(result)

elif operator == "/":
    result = number_1 / number_2
    print(result)

else:
    print(f"{operator} is not a valid operator")



