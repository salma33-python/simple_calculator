print("Welcome to the Simple Calculator!")

# Display operations
print("Select an operation:")
print("1 - Addition (+)")
print("2 - Subtraction (-)")
print("3 - Multiplication (*)")
print("4 - Division (/)")

# Get user input
operation = input("Enter the operation number (1/2/3/4): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform calculation based on user choice
if operation == "1":
    result = num1 + num2
    print(f"Result: {num1} + {num2} = {result}")

elif operation == "2":
    result = num1 - num2
    print(f"Result: {num1} - {num2} = {result}")

elif operation == "3":
    result = num1 * num2
    print(f"Result: {num1} * {num2} = {result}")

elif operation == "4":
    if num2 == 0:
        print("Error! Division by zero is not allowed.")
    else:
        result = num1 / num2
        print(f"Result: {num1} / {num2} = {result}")

else:
    print("Invalid input! Please enter a valid operation number."
