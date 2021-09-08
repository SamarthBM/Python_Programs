'''
* @Author: Samarth BM.
* @Date: 2021-09-08 23:25  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-08 23:42
* @Title: To print the power of two till the entered range and should be > 0 and < 31.
'''

from math import pow

power_of_two = int(input("Enter a range to get the power of two: "))

# Checking if entered range is within the limit.
if(0<power_of_two<31):
    for i in range (power_of_two):      # Iterating till the entered range.
        print("2 ^ ",i," = ",pow(2,i))
else:
    print("Enter the proper range")
