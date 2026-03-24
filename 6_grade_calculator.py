def grade_calculator():
    try:
        marks = []

        #asking marks in 5 subjects
        for i in range(1, 6):
            m = int(input(f"Enter marks for subject {i} (0-100): "))
            #ensure that marks must between 0 to 100
            if m < 0 or m > 100:
                print("Marks must be between 0 and 100")
                return
            marks.append(m)

        #display marks for each subject
        print("\nMarks in each subject:")
        for i in range(5):
            print(f"Subject {i+1}: {marks[i]}")

        # calculating the total marks out of 500
        total_marks = sum(marks)
        print("Total Marks:", total_marks, "/500")

        #calculating the percentage
        percentage = (total_marks / 500) * 100
        print("Percentage:", round(percentage, 2), "%")

        #checking you are pass or fail in all subjects
        if all(m >= 40 for m in marks):
            result = "Pass"
        else:
            result = "Fail"

        #calculates the grade based on the percentage
        if percentage >= 90:
            grade = "A+ (Outstanding)"
        elif percentage >= 80:
            grade = "A (Excellent)"
        elif percentage >= 70:
            grade = "B (Good)"
        elif percentage >= 60:
            grade = "C (Average)"
        elif percentage >= 50:
            grade = "D (Pass)"
        else:
            grade = "F (Fail)"

        print("Grade:", grade)
        print("Result:", result)

    except ValueError:
        print("Enter valid integer marks input.....")

grade_calculator()