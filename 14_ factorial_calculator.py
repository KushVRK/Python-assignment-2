# Factorial Calculator

try:
    num = int(input("Enter a number: "))

    #checking for negative numbers
    if num < 0:
        print("Factorial is not defined for negative numbers!")

    elif num == 0:
        print("0! = 1 ")

    else:
        result = 1 #used to store factorial value
        steps = []  #creating an empty list to store numbers for display

        for i in range(num, 0, -1):
            result = result * i
            steps.append(str(i)) #appending the numbers to stepos by converting them into a string

        # join steps of string character with x to show full calculation
        step_str = " x ".join(steps)
        print(f"\n{num}! = {step_str} = {result}")

except ValueError:
    print("Invalid input! Please enter a whole number.")