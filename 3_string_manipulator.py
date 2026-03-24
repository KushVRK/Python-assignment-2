def string_manipulation():
    try:
        str1 = input("Enter a sentence: ")
        # if u does'nt enter any sentence
        if str1 == "":
            raise ValueError

        print("\n -----------String Manipulation------------------")

        
        print("Original sentence:", str1)

        # Total characters include spaces
        print("Characters (with spaces):", len(str1))

        # Total characters Excludes spaces
        print("Characters (without spaces):", len(str1.replace(" ", "")))

        # Total words
        print("Words:", len(str1.split()))

        # Converts the sentence to Uppercase
        print("UPPERCASE:", str1.upper())

        # Converts the sentence Lowercase
        print("lowercase:", str1.lower())

        # Title Case
        print("Title Case:", str1.title())

        # First word in a sentence
        print("First word:", str1.split()[0])  # returns first word not letter

        # Last word in a sentence
        print("Last word:", str1.split()[-1])

        # Reversed sentence
        print("Reversed:", str1[::-1])

    except ValueError:
        print("Enter the valid Sentence......")

    # finally runs at last
    finally:
        print("        ESCN       ")

# Fuction call
string_manipulation()