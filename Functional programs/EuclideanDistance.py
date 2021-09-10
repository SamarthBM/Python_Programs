"""
* @Author: Samarth BM.
* @Date: 2021-09-10 20:40  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-10 20:40  
* @Title: :To calculate euclidean distance of x and y co-ordinates.
"""

import math as m

def euclidean_distance():

    """
    Descripton:
        This function is used to calculate distance using euclidean formulae.
        It takes two inputs i.e x and y co-ordinates.
        Math.sqrt and Maht.pow function is used to calculate the distance.

    """    
    
    # Userinput for x and y co-ordinates.
    x = float(input("Enter the value of x-coordinate: "))
    y = float(input("Enter the value of y-coordinate: "))

    # Calculating the euclidean distance.
    result = m.sqrt( m.pow(x,2) + m.pow(y,2) )
    print("Euclidean distance for given co-ordinates is: ",result)

euclidean_distance()
