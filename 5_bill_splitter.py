def bill_splitter():
    try:
        bill = float(input("Enter total bill: "))
        persons = int(input("Number of people: "))
        tax_percent = float(input("Tax percentage: "))
        tip_percent = float(input("Tip percentage: "))

        #avoids division by zero and ensures valid user input
        if bill <= 0 or persons <= 0 or tax_percent < 0 or tip_percent < 0:
            raise ValueError

        # Subtotal
        subtotal = bill

        # Tax amount
        tax_amount = (tax_percent / 100) * subtotal

        # Bill after tax
        after_tax = subtotal + tax_amount

        # Tip amount
        tip_amount = (tip_percent / 100) * after_tax

        # Total bill
        total_bill = after_tax + tip_amount

        # Amount per person
        per_person = total_bill / persons

        print("\n=== BILL BREAKDOWN ===")
        print("Subtotal:    ₹", round(subtotal, 2))
        print(f"Tax ({tax_percent}%):   ₹", round(tax_amount, 2))
        print("After tax:   ₹", round(after_tax, 2))
        print(f"Tip ({tip_percent}%):   ₹", round(tip_amount, 2))
        print("Total:       ₹", round(total_bill, 2))
        print("Per person:  ₹", round(per_person, 2))

    #ZeroDivisionError except is not required as we avoided it in our logic of code only
    # except ZeroDivisionError:
    #     print("Enter the correct number of people...")
    except ValueError:
        print("Enter the valid user input .....")

bill_splitter()