def personal_bio_card():
    #creating try and except blocks as u instructed us use this to avoid edge cases and invalid inputs
    try:
        #try block contains code
        name = input("Enter your Name: ")
        age=int(input("Enter your age: "))
        Address=input("Enter your current Location: ")
        Hobby=input("enter your hobby: ")

        print("")
        print("---------------Personal Bio Card-------------------")
        print(f"Name: {name}")
        print(f"age: {age}")
        #because age will not be negative
        if age<0:
            #so if age is negative it calls valueerror msg declared below in except block
            raise ValueError
        print(f"Address: {Address}")
        print(f"Hobbies: {Hobby}")
        print("---------------------------------------------------")

    except ValueError:
        '''this block will run automically if any errors occured in code present in try block. 
        It also contains different type of except like ZeroDivisionError, keyError, FileNotfoundError.
        Here we used ValueError if user input types wrong datatype'''
        print("Invalid input....Please enter correct input details")
    finally:
        #it will always run automatically after above blocks without depending on errors
        print("")
        print("Done with 1st question of assignment")


personal_bio_card()
