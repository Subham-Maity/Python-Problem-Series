"""So here we did like this
Check if the year is divisible by 400 or 4 but not 100, DISPLAY "is a leap year", Otherwise, DISPLAY ": is not a leap year."""""

year = int(input("Enter your Year:\n"))
 
leap_year = "It's a leap year !"
common_year = "It's not a leap year"
if year % 4 == 0:
    if year % 100 != 0:
        print(leap_year)
    elif year % 400 == 0:
        print(leap_year)
    else:
        print(common_year)
else:
    print(common_year)


