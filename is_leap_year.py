while True:
  year = input("Please enter a 4 digit year: ")
  if year.isdigit() == True:
    if (int(year) % 4 == 0) and (int(year) % 100 != 0):
      print(year, "is a leap year")
      break
    elif int(year) % 400 == 0:
      print(year, "is a leap year")
      break
    else:
      print(year, "is not a leap year.")
      break
  else:
    print("Please Enter a valid year.")