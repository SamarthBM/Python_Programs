'''
* @Author: Samarth BM.
* @Date: 2021-09-08 21:19  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-08 21:34
* @Title: To check whether entered year is leap year or not
'''

year = int(input("Enter a year to check"))

# Condition to check for valid year.
if (year <= 999 or year > 9999):
    print("Enter a valid year")
    
# Condition to check for leap year.    
else:
    if year % 4 == 0:
        if year % 100 != 0 or year % 400 == 0:
            print(" Its a leap year")
        else:
            print("Its not a leap year")
    else:
         print("Its not a leap year")

