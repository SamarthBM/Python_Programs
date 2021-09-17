'''
* @Author: Samarth BM.
* @Date: 2021-09-17 23:34  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-17 23:34
* @Title: To create array and print the elements in reverse order.
'''

from logging import exception
from LogHandler import logger

def print_array(array):
    """
    Description:
        This function is to print the elements of array in entered order.

    Args:
        array: Array to be printed.
    """    

    try:
        for elements in range(len(array)):
            print(array[elements])
        logger.info("Original array printed")

    except exception():
        logger.error("Invalid input")

def reverse_array(rev_array):
    """
    Description:
        This function is to print the elements of array in reversed order.

    Args:
        rev_array: Array to be printed.
    """ 

    try:
        for elements in range(len(rev_array)-1,-1,-1):
            print(rev_array[elements])
        logger.info("Reversed array printed")

    except exception():
        logger.error("Invalid input")

    
if __name__ == "__main__":

    try:
        array1 = [1,2,3,4,5]

        print("Original array is: ")
        print_array(array1)
        print("Reversed array is: ")
        reverse_array(array1)
        
    except exception():
        logger.error("Invalid input")
