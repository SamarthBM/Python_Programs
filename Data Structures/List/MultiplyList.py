'''
* @Author: Samarth BM.
* @Date: 2021-09-19 13:51  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-19 13:51
* @Title: To multiply all values in a list.
'''

from LogHandler import logger
from math import prod

def multiply_list():
    """
    Description: 
        This function is to multiply all values in list.
    """
    try:
        my_list = [2, 5, 6]

        print("Product of the list is:", prod(my_list))
        logger.info("Values multiplied")

    except Exception:
        logger.error("Invalid Input")

if __name__ == "__main__":
    multiply_list()       