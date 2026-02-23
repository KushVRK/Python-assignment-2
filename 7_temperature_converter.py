def temperature_converter():
    while True:
        try:
            print("\n------ Temperature Converter ------")
            print("1. Celsius to Fahrenheit")
            print("2. Fahrenheit to Celsius")
            print("3. Celsius to Kelvin")
            print("4. Kelvin to Celsius")
            print("5. Fahrenheit to Kelvin")
            print("6. Kelvin to Fahrenheit")
            print("7. Exit")

            choice = int(input("Enter your choice between 1-7: "))

            #exit condition
            if choice == 7:
                print("Exiting Temperature Converter......")
                break

            #check for valid choice
            if choice < 1 or choice > 7:
                print("Enter a valid choice between 1 and 7")
                continue

            temp = float(input("Enter temperature value: "))

            #Celsius to Fahrenheit
            if choice == 1:
                result = (temp * 9/5) + 32
                print("Temperature in Fahrenheit:", round(result, 2))

            #Fahrenheit to Celsius
            elif choice == 2:
                result = (temp - 32) * 5/9
                print("Temperature in Celsius:", round(result, 2))

            #Celsius to Kelvin
            elif choice == 3:
                result = temp + 273.15
                print("Temperature in Kelvin:", round(result, 2))

            #Kelvin to Celsius
            elif choice == 4:
                result = temp - 273.15
                print("Temperature in Celsius:", round(result, 2))

            #Fahrenheit to Kelvin
            elif choice == 5:
                result = (temp - 32) * 5/9 + 273.15
                print("Temperature in Kelvin:", round(result, 2))

            #Kelvin to Fahrenheit
            elif choice == 6:
                result = (temp - 273.15) * 9/5 + 32
                print("Temperature in Fahrenheit:", round(result, 2))

        except ValueError:
            print("Enter valid numeric input only.....")
            continue   # THIS is the key fix

temperature_converter()