"""
* @Author: Samarth BM.
* @Date: 2021-09-10 21:08  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-10 21:08   
* @Title: :To find the roots of a quadractic equation.
"""

import math as m

def quadratic_equation():

    """
    Description:
        In this function the two roots of quadratic equation is found.
        a, b, c are the three inputs to find the delta value.
        The value of delta should be greater than 0 to have two real roots.

    """    

    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    c = int(input("Enter the value of c: "))

    # Getting the value of delta.
    delta = (b * b - 4 * a * c)

    # Finding the roots if value of delta is greater than 0.
    if(delta > 0):
        root1 = (-b + m.sqrt(delta)) / (2 * a)
        root2 = (-b - m.sqrt(delta)) / (2 * a)

        print("First root of equation is: ",root1)
        print("Second root of equation is: ",root2)
    else:
        print("There are no real two roots for the given values")

quadratic_equation()   


