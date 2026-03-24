# Simple ATM Simulator with transaction history - Bonus 

balance = 10000
min_balance = 500
history = []  #to stores all transactions

print("Welcome to ATM")

while True:
    # show menu
    print("\n1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transaction History")
    print("5. Exit")

    choice = input("\nEnter choice: ")

    if choice == "1":
        print(f"Your's current balance is: Rs.{balance}")

    elif choice == "2":
        try:
            amount = int(input("Enter amount to deposit: "))
            if amount <= 0:
                print("Amount should be greater than 0....")
            else:
                balance = balance + amount
                print(f"Deposit successful... Your New balance: Rs.{balance}")
                # save this transaction to history
                history.append(f"Deposited  Rs.{amount}  | Balance: Rs.{balance}")
        except ValueError:
            print("Invalid user input..... please enter a number.")

    elif choice == "3":
        try:
            amount = int(input("Enter an amount to be withdraw: "))
            if amount <= 0:
                print("Amount should be greater than 0...")
            # check if enough balance will remain after withdrawal
            elif balance - amount < min_balance:
                print(f"Cannot withdraw the amount... Minimum balance of Rs.{min_balance} must remain.")
                print(f"You can withdraw maximum of Rs.{balance - min_balance}")
            else:
                balance = balance - amount
                print(f"Withdrawal successful..... Your new balance: Rs.{balance}")
                # save this transaction to history
                history.append(f"Withdrawn  Rs.{amount}  | Balance: Rs.{balance}")
        except ValueError:
            print("Invalid user input...... Enter a number.")

    elif choice == "4":
        print("\n=========Transaction History========== ")
        if len(history) == 0:
            print("No transactions yet........")
        else:
            for i, record in enumerate(history, 1):
                print(f"{i}. {record}")

    elif choice == "5":
        print("Thank you for using ATM.....")
        break

    else:
        print("Invalid choice........ Please enter 1 to 5.")