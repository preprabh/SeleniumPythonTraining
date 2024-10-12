# Find if a year is leap year or not

year = int(input("Please enter a year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year!!!")
        else:
            print("Not a leap year")
    else:
        print("Leap Year!!!")
else:
    print("Not a leap year")
