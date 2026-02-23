# Number System Functions

def factorial(n):
    if n < 0:
        return "Not defined for negative numbers"
    if n == 0:
        return 1
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

def fibonacci(n):
    if n <= 0:
        return "Enter positive number"
    if n == 1:
        return 0
    if n == 2:
        return 1
    a, b = 0, 1
    for i in range(2, n):
        a, b = b, a+b
    return b

def sum_of_digits(n):
    n = abs(n)  # handle negative numbers
    total = 0
    for ch in str(n):
        total += int(ch)
    return total

def reverse_number(n):
    negative = n < 0
    reversed_str = str(abs(n))[::-1]
    result = int(reversed_str)
    if negative:
        return -result
    return result

def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    total = 0
    for d in digits:
        total += int(d) ** power
    return total == n

def gcd(a, b):
    # using euclidean algorithm
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    # lcm formula using gcd
    return abs(a * b) // gcd(a, b)

def is_perfect_number(n):
    if n <= 1:
        return False
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total == n

def math_menu():
    print("Welcome to Number System Functions")

    while True:
        print("\n1.  Factorial")
        print("2.  Prime Checker")
        print("3.  Fibonacci")
        print("4.  Sum of Digits")
        print("5.  Reverse Number")
        print("6.  Armstrong Checker")
        print("7.  GCD")
        print("8.  LCM")
        print("9.  Perfect Number Checker")
        print("10. Exit")

        choice = input("\nEnter choice: ")

        try:
            if choice == "1":
                n = int(input("Enter number: "))
                print(f"Factorial: {factorial(n)}")

            elif choice == "2":
                n = int(input("Enter number: "))
                if is_prime(n):
                    print(f"{n} is a PRIME number")
                else:
                    print(f"{n} is NOT a prime number")

            elif choice == "3":
                n = int(input("Enter position (n): "))
                print(f"Fibonacci({n}) = {fibonacci(n)}")

            elif choice == "4":
                n = int(input("Enter number: "))
                print(f"Sum of digits: {sum_of_digits(n)}")

            elif choice == "5":
                n = int(input("Enter number: "))
                print(f"Reversed: {reverse_number(n)}")

            elif choice == "6":
                n = int(input("Enter number: "))
                if is_armstrong(n):
                    print(f"{n} is a Armstrong number")
                else:
                    print(f"{n} is NOT a Armstrong number")

            elif choice == "7":
                a = int(input("Enter the first number: "))
                b = int(input("Enter the second number: "))
                print(f"GCD: {gcd(a, b)}")

            elif choice == "8":
                a = int(input("Enter the first number: "))
                b = int(input("Enter the second number: "))
                print(f"LCM: {lcm(a, b)}")

            elif choice == "9":
                n = int(input("Enter the number: "))
                if is_perfect_number(n):
                    print(f"{n} is a Perfect number")
                else:
                    print(f"{n} is NOT a perfect number")

            elif choice == "10":
                print("Exited........")
                break

            else:
                print("Invalid choice! Enter 1 to 10.")

        except ValueError:
            print("Invalid user input...... Enter numbers only.")

# run the menu
math_menu()