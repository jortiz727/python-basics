import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

def power(x, y):
    return x ** y

def sqrt(x):
    return x ** 0.5


# show a menu of operations (add, subtract, ... , quit)
# ask the user to pick one
# if they picked q, quit -> stop
# ask for the number(s) (sqrt only needs one)
# call the matching function
# print the result
# go back to the menu

while True:
    print("\n Calculator Menu")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("q. Quit")

    choice = input("Enter your choice (1-6 or q to quit): ")

    if choice == 'q':
        print("Exiting the calculator. Goodbye!")
        break
    elif choice == "1":
        print("You chose addition.")
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))
        print(f"The result is: {add(x, y)}")
    elif choice == "2":
        print("You chose subtraction.")
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))
        print(f"The result is: {subtract(x, y)}")
    elif choice == "3":
        print("You chose multiplication.")
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))
        print(f"The result is: {multiply(x, y)}")
    elif choice == "4":
        print("You chose division.")
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))
        print(f"The result is: {divide(x, y)}")
    elif choice == "5":
        print("You chose power.")
        x = float(input("Enter the base number: "))
        y = float(input("Enter the exponent: "))
        print(f"The result is: {power(x, y)}")
    elif choice == "6":
        print("You chose square root.")
        x = float(input("Enter the number: "))
        print(f"The result is: {sqrt(x)}")
    else:
        print("Invalid choice. Please select a valid option from the menu.")
