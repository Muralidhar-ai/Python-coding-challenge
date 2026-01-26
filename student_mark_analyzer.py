print("----- Student Result Analyzer -----")

name = input("Enter Your Name: ")
mark = int(input("Enter Your Marks: "))

if mark >= 0 and mark <= 100:
    print("\n---- Result Calculation ----")
    print("Name:", name)
    print("Marks:", mark)

    if mark >= 60:
        print("Result: PASS")

        if mark >= 90:
            print("Grade: A")
        elif mark >= 75:
            print("Grade: B")
        else:
            print("Grade: C")
    else:
        print("Result: FAIL")
        print("Grade: F")

else:
    print("Invalid Mark")
