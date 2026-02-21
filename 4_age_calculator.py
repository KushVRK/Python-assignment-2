#importing datetime to know present year
from datetime import datetime

def age_calculator():
    try:
        birth_year=int(input("Enter your Birth Year: "))
        present_year=datetime.now().year
        #TO avoid user input of negative birth year or more than present year 
        if birth_year<0 or birth_year>present_year:
            raise ValueError
        age=present_year-birth_year
        print("Your age is ",age)
    #to handle wrong user input
    except ValueError:
        print("Enter your correct birth year......")
    #optional final block
    finally:
        print("We can't directly ask your age so we asked your birth year.........")

age_calculator()