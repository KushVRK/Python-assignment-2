def simple_calculator():
    try:
        #codes inside try block to build simple calculator
        a=int(input("enter the 1st number: ")) 
        b=int(input("enter the 2nd number: "))
        o=input("enter the Operation (+,-,*,/,%): ")
        print("")
        #using if elif condition to build the simple calculator
        if o=='+':
            print("Result=",a+b)
        elif o=='-':
            print("Result=",a-b)
        elif o=='*':
            print("Result=",a*b)
        elif o=='/':
            print("Result=",a/b)
        elif o=='%':
            print("Result=",a%b)
        else:
            print("Invalid Operator")

    #used to avoid user input errors
    except ValueError:
        print("Enter correct input values..........")

    #used to avoid error if user tries to divide (/) or find remainder (%) by zero
    except ZeroDivisionError:
        print("division by zero is not allowed")

simple_calculator()

    
