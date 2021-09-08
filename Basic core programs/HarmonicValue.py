'''
* @Author: Samarth BM.
* @Date: 2021-09-08 23:51  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-08 21:34
* @Title: To get the harmonic value for entered range.
'''

harmonic_range = int(input("Enter a range to get harmonic value: "))
harmonic_value = 0

# To start the iteration from 1 till the entered range.
for i in range(1,harmonic_range+1):
    if harmonic_range == 0: 
        print("Please enter value greater than 0")
        break
    else:
        harmonic_value += 1/i

print("Harmonic value till entered range is ",harmonic_value)
        