def bill_splitter():
    try:
        bill=float(input("Enter your Total bill: "))
        persons=int(input("Enter the total number of people : "))
        #avoids division by zero and ensures vailid user input
        if bill<=0 or persons<=0:
            raise ValueError
        amount=bill/persons
        print("The amount should be paye by each person is: ",round(amount,2))
    #ZeroDivisionError except is not required as we avoided it in our logic of code only
    # except ZeroDivisionError:
    #     print("Enter the correct number of people...")
    except ValueError:
        print("Enter the valid user input .....")

bill_splitter()


