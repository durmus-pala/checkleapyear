year = input("Please Enter year to check: ")
if (int(year) % 4 == 0) and (int(year) % 100 != 0):
    print(year, "is a leap year.")
elif int(year) % 400 == 0:
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
    
            