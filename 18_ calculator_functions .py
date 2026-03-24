import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    # cant divide by zero
    if b == 0:
        return "Division by zero is not allowed... retry with different divisor"
    return a / b

def modulus(a, b):
    if b == 0:
        return "Division by zero is not allowed... retry with different divisor"
    return a % b

def power(a, b):
    return a ** b

def square_root(a):
    # cant do square root of negative number
    if a < 0:
        return "Square root of negative number is not allowed..."
    return math.sqrt(a)

def percentage(a, b):
    # calculates what percent a is of b
    if b == 0:
        return "Cannot calculate percentage... b cannot be zero"
    return (a / b) * 100

def calculator():
    print("Welcome to the Calculator.......")

    while True:
        # show menu
        print("\n1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Modulus")
        print("6. Power")
        print("7. Square Root")
        print("8. Percentage")
        print("9. Exit")

        choice = input("\nChoose which fuction do you want to perform (1-9): ")

        if choice == "9":
            print("You are exited from calculator")
            break

        if choice in ["1","2","3","4","5","6"]:
            try:
                a = float(input("Enter the first number: "))
                b = float(input("Enter the second number: "))

                if choice == "1":
                    result = add(a, b)
                elif choice == "2":
                    result = subtract(a, b)
                elif choice == "3":
                    result = multiply(a, b)
                elif choice == "4":
                    result = divide(a, b)
                elif choice == "5":
                    result = modulus(a, b)
                elif choice == "6":
                    result = power(a, b)
                print("functions runned succesfully")
                print(f" So Result={result}")

            except ValueError:
                print("Invalid user input...... Enter numbers only.")

        # square root only needs one number
        elif choice == "7":
            try:
                a = float(input("Enter the number: "))
                result = square_root(a)
                print("functions runned succesfully")
                print(f" So Result={result}")
            except ValueError:
                print("Invalid user input...... Enter numbers only.")

        # percentage needs two numbers
        elif choice == "8":
            try:
                a = float(input("Enter  your's value to find percentage: "))
                b = float(input("Enter the total value: "))
                result = percentage(a, b)
                print("functions runned succesfully")
                print(f" So Result={round(result,3)}%")
            except ValueError:
                print("Invalid user input...... Enter numbers only.")

        else:
            print("Invalid choice...... Enter 1 to 9 only.")

# calling the function
calculator()