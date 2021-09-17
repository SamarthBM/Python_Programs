'''
* @Author: Samarth BM.
* @Date: 2021-09-18 00:11  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-18 00:11
* @Title: To remove element first occurence in array .
'''

from logging import exception
from LogHandler import logger

def remove_element(array, element):
    """
    Description:
        This function is to remove the first occurence in array.

    Args:
        array: Array which stores elements.
        element: Element to be removed.
    """    
    
    try:
        for i in range(len(array)):
                if array[i] == element:
                    array.remove(element)
                    break
        print("Array after removing {} is {} ".format(element, array))

    except exception:
        logger.error("Invalid input")

if __name__ == "__main__":

    try:
        array1 = [1,2,3,2,4,1,3,5,7]
        element = 3

        remove_element(array1, element)
    
    except exception:
        logger.error("Invalid input")
                