def is_leap(year):
    leap = False
    
    # Write your logic here
    # constraint

    if year >= 1900 and year <= 10**5:
        if year in [1800, 1900, 2100, 2200, 2300, 2500]:
            leap = False
        elif year % 4 == 0 or year % 400 ==0 :
            leap = True
        elif year % 100 == 0 :
            leap = False
    
    return leap

year = int(input())
print(is_leap(year))


