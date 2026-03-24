# importing to help with median and mode
from statistics import median, mode, StatisticsError

try:
    count = int(input("How many numbers? "))

    if count <= 0:
        print("Please enter a count greater than 0!")
    else:
        #creating an empty list to store the numbers
        numbers = []

        # storing the user entered numbers into the list
        for i in range(1, count+1):
            num = float(input(f"Enter number {i}: "))
            numbers.append(num)

        # calculate everything
        total = sum(numbers)
        average = total / count
        maximum = max(numbers)
        minimum = min(numbers)

        # calculate median
        med = median(numbers)

        # mode can fail if all numbers appear same times
        try:
            mod = mode(numbers)
        except StatisticsError:
            mod = "No mode (all numbers appear equally)"

        # showing the results
        print("\n--- Results ---")
        print(f"Sum     : {total}")
        print(f"Average : {average}")
        print(f"Maximum : {maximum}")
        print(f"Minimum : {minimum}")
        print(f"Median  : {med}")
        print(f"Mode    : {mod}")

except ValueError:
    print("Invalid input! Please enter numbers only..........")