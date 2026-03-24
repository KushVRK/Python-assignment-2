# Leap Year Checker
# This program checks whether a given year is a leap year or not
def check_leap_year():
    try:
    
        year = int(input("Enter a year: "))

        # A year is always positive
        if year <= 0:
            print("Please enter a valid positive year.")
            return

        # Check the leap year conditions step by step
        # Rule 1: divisible by 400 -> always a leap year
        # Rule 2: divisible by 100 but not 400 -> NOT a leap year
        # Rule 3: divisible by 4 but not 100 -> leap year
        # Rule 4: not divisible by 4 at all -> NOT a leap year

        if year % 400 == 0:
            is_leap = True
            reason = f"{year} is divisible by 400, so it IS a leap year."

        elif year % 100 == 0:
            is_leap = False
            reason = f"{year} is divisible by 100 but NOT by 400, so it is NOT a leap year."

        elif year % 4 == 0:
            is_leap = True
            reason = f"{year} is divisible by 4 and not by 100, so it IS a leap year."

        else:
            is_leap = False
            reason = f"{year} is not divisible by 4, so it is NOT a leap year."

        # Display the result
        if is_leap:
            print(f"\nYear: {year}")
            print("Result: Leap Year")
        else:
            print(f"\nYear: {year}")
            print("Result: NOT a Leap Year")

        print(f"Reason: {reason}")

    except ValueError:
        # to handle invalid user input
        print("Invalid user input.........")
check_leap_year()