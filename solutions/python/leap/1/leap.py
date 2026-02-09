def leap_year(year):
    leap = str(year) + " is a leap year!"
    notleap = str(year) + " was not a leap year"
    
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
    
