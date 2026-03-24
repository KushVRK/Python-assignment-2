def ticket_pricing_system():
    print("Welcome to Movie Ticket Booking")
    print("--------------------------------")

    try:
        age = int(input("Enter age: "))
        day = input("Enter day of week: ").strip().lower()
        tickets = int(input("Enter number of tickets: "))

        # basic validation
        if age < 0 or tickets <= 0:
            print("Invalid age or ticket count!")
            return

        # find base price based on age
        if age < 3:
            base_price = 0
            category = "Free"
        elif age <= 12:
            base_price = 150
            category = "Child"
        elif age <= 59:
            base_price = 300
            category = "Adult"
        else:
            base_price = 200
            category = "Senior"

        # check if weekend or weekday for discount
        weekend = ["friday", "saturday", "sunday"]
        weekdays = ["monday", "tuesday", "wednesday", "thursday"]

        if day in weekend:
            discount = base_price * 0.20
            day_type = "Weekend"
        elif day in weekdays:
            discount = 0
            day_type = "Weekday"
        else:
            print("Invalid day entered!")
            return

        # calculate final prices
        price_per_ticket = base_price - discount
        total = price_per_ticket * tickets

        # show results
        print("\n--- Bill Summary ---")
        print(f"Category      : {category}")
        print(f"Base Price    : Rs.{base_price}")
        print(f"Day           : {day_type} (Discount: Rs.{discount})")
        print(f"Price/Ticket  : Rs.{price_per_ticket}")
        print(f"Tickets       : {tickets}")
        print(f"Total Amount  : Rs.{total}")

    except ValueError:
        print("Please enter valid numbers for age and tickets.")

ticket_pricing_system()