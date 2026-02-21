def string_manipulation():
    try:
        str1=input("Enter a String: ")
        #if u does'nt enter any string 
        if str1=="":
            raise ValueError
        print("\n -----------String Manipulation------------------")
        print("Original String: ",str1)
        print("Length of the String: ", len(str1))
        print("Uppercase: ", str1.upper())
        print("Lowercase: ", str1.lower())
        print("Title: ", str1.title())
        print("Reversed String: ", str1[::-1])
        print("First Character in a String: ",str1[0])
        print("Last Character in a String: ",str1[-1])
        print("First Word in a String: ",str1.split()[0]) #returns first word not letter
        print("Last Word in a String: ",str1.split()[-1])
    except ValueError:
        print("Enter the valid String......")
    #finally runs at last
    finally:
        print("        ESCN       ")

#Fuction call
string_manipulation()