# each patterns are defined by following
def pattern1(n):
    # each row prints numbers 1 to row number
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end=" ")
        print()

def pattern2(n):
    # each row prints the row number, row number of times
    for i in range(1, n+1):
        for j in range(i):
            print(i, end=" ")
        print()

def pattern3(n):
    # each row counts down from n-i to 1
    for i in range(n):
        for j in range(n-i, 0, -1):
            print(j, end=" ")
        print()

def pattern4(n):
    # pyramid shape so need spaces before numbers
    for i in range(1, n+1):
        # spaces to make it look like pyramid
        spaces = " " * (n - i)
        print(spaces, end="")

        # going up 1 to i
        for j in range(1, i+1):
            print(j, end="")

        # coming back down i-1 to 1
        for j in range(i-1, 0, -1):
            print(j, end="")

        print()

try:
    print("Pattern 1: 1 / 1 2 / 1 2 3 ...")
    print("Pattern 2: 1 / 2 2 / 3 3 3 ...")
    print("Pattern 3: reverse of patern 15")
    print("Pattern 4: Pyramid numbers")

    choice = int(input("\nEnter pattern number (1-4): "))
    height = int(input("Enter height: "))

    if height <= 0:
        print("Height must be greater than 0!")
    elif choice == 1:
        pattern1(height)
    elif choice == 2:
        pattern2(height)
    elif choice == 3:
        pattern3(height)
    elif choice == 4:
        pattern4(height)
    else:
        print("Invalid pattern choice!")

except ValueError:
    print("Please enter valid numbers only!")