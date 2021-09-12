"""
* @Author: Samarth BM.
* @Date: 2021-09-12 21:11
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-12 21:11 
* @Title: :To generate random and unique coupon numbers.
"""

import random

def coupon_numbers():
    """
    Description:
        This function is used to generate random and unique coupon numbers.
        User input is taken for number and range of coupon numbers.
        Random fuction is used to generate random coupon numbers.
        Set is used to get the unique coupon numbers.

    """    

    try:
        number_of_coupon = int(input("Enter the number of coupons to print: "))
        coupon_range = int(input("Enter the range of coupon numbers: "))

        coupons = [] # Array to store all coupon numbers.

        for number in range(number_of_coupon):
            random_coupons = random.randint(0,coupon_range)
            coupons.append(random_coupons)

        # Set is used to print unique numbers.
        unique_number = set(coupons)
        print("Unique coupon numbers are: ", unique_number)

    except Exception as e:
        print("Exception occured is: ",e)


if __name__ == "__main__":
    coupon_numbers()