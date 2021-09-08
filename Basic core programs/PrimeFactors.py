'''
* @Author: Samarth BM.
* @Date: 2021-09-09 00:18  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-09 00:18
* @Title: To print all the prime factors of entered number.
'''

number = int(input("Enter a number to get its prime factors: "))
prime_factors = []
divisor = 2

# Looping till the quotient is less than divisor.
while divisor <= number:
    if number % divisor == 0:
        prime_factors.append(divisor)
        number = number/divisor
    else:
        divisor += 1

print("Prime factors of entered number is: ",prime_factors)