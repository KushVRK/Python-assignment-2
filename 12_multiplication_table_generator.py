# Multiplication Table Generator

try:
    #taking the user input
    num = int(input("Enter number: "))
    end = int(input("Enter range (end): "))
    
    #the range should not be zero or less than that
    if end <= 0:
        print("Range must be greater than 0!")
    else:
        print(f"\nMultiplication Table of {num}")
        print("---------------------------------------")
        for i in range(1, end+1):
            print(f"{num} x {i} = {num * i}")

except ValueError:
    print("Invalid user input......")
    print("Enter only numeric inputs")
    

# bonus - full 1 to 10 grid
print("\n--- Bonus: Full Multiplication Table (1-10) ---\n")


# Multiplication Table Grid (1 to 10)

# Print top header row
print("        ", end="") #where the space is given to adjust the table into grid format
for i in range(1, 11):
    print(i, end="\t") # where end="\t gives u the tap space for each number"
print()

# Print separator line to arrange it in grid format
print("-----------------------------------------------------------------------------------------------")

# Print table rows
for i in range(1, 11):
    print(i, end="\t")  # Row header
    for j in range(1, 11):
        print(i * j, end="\t")
    print()