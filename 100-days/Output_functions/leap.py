def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    # Don't change the function name.
    else:
        return False

def is_leap_yearV2(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)