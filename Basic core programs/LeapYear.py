'''
* @Author: Samarth BM.
* @Date: 2021-09-08 21:19  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-10 13:01
* @Title: To check whether entered year is leap year or not
'''

import re

year = input("Enter a year to check: ")

# Condition to check for valid year.
if re.match("^[0-9]{4}$", year):

    if int(year) % 4 == 0:
        if int(year) % 100 != 0 or int(year) % 400 == 0:
            print(" Its a leap year")
        else:
            print("Its not a leap year")
    else:
         print("Its not a leap year")

else:
    print("Enter a valid year")
   

