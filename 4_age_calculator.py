#importing datetime to know present date
from datetime import datetime

def age_calculator():
    try:
        #asking exact birth details 
        day = int(input("Enter your Birth Day: "))
        month = int(input("Enter your Birth Month: "))
        year = int(input("Enter your Birth Year: "))

        #creating birth date using datetime
        birth_date = datetime(year, month, day)
        present_date = datetime.now()

        #TO avoid invalid birthdate input
        if birth_date > present_date:
            raise ValueError

        #calculating exact age difference
        age_days = (present_date - birth_date).days
        age_years = age_days // 365
        age_months = age_days // 30
        age_hours = age_days * 24
        age_minutes = age_hours * 60

        print(" Current age:", age_years, "years")
        print("Age in months:", age_months)
        print("Age in days (approx 365 days/year):", age_days)
        print("Age in hours :", age_hours)
        print(" Age in minutes:", age_minutes)

        #years remaining to reach 100
        years_to_100 = 100 - age_years
        if years_to_100 > 0:
            print("Years until age 100 :", years_to_100)
        else:
            print("You are already 100 or above")

    #to handle wrong user input
    except ValueError:
        print("Enter valid birth date details......")

    #optional final block
    finally:
        print("We can't directly ask your age so we asked your birth date.........")

age_calculator()


