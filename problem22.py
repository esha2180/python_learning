year = int(input("Enter a year: "))

if (year % 400 == 0) and (year % 100 == 0) :
    print("This year is a leap year")
elif (year % 4 == 0) and (year % 100 != 0):
    print("This year is a leap year")
else :
    print("This year is not a leap year")