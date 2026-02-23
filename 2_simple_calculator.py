def simple_calculator():
    try:
        #codes inside try block to build simple calculator
        a=int(input("enter the 1st number: ")) 
        b=int(input("enter the 2nd number: "))
        print("")
        #using if elif condition to build the simple calculator
        print("Results:")
        print(f"{a} + {b} = ",a+b)
        print(f"{a} - {b} = ",a-b)
        print(f"{a} * {b} = ",a*b)

        # division shows 2 decimal places
        if b == 0:
            print("Division  : division by zero is not allowed")
        else:
            print(f"{a} / {b} = ",round(a/b, 2))

        # modulus also cant be done with zero
        if b == 0:
            print("Modulus   : division by zero is not allowed")
        else:
            print(f"{a} % {b} = ",a%b)

        print(f"{a} ^ {b} = ",a**b)

    #used to avoid user input errors
    except ValueError:
        print("Enter correct input values..........")

    #used to avoid error if user tries to divide (/) or find remainder (%) by zero
    except ZeroDivisionError:
        print("division by zero is not allowed")
#calling the function
simple_calculator()