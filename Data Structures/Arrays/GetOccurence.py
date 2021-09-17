'''
* @Author: Samarth BM.
* @Date: 2021-09-17 23:51  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-17 23:51
* @Title: To get the occurence of a element in array.
'''

from logging import exception
from LogHandler import logger

def get_occurence(array, element):
    """
    Description:
        This function to get the occurence of a element in array.

    Args:
        array: Array which holds elements.
        element: Element to search for occurence.
        
    """    
    
    try:
        count = 0

        for i in range(len(array)):
            if array[i] == element:
                count += 1

        print("Element {} occured for {} times.".format(element,count))
        logger.info("Element {} occured for {} times.".format(element,count))

    except exception:
        logger.error("Invalid")


if __name__ == "__main__":

    try:

        array1 = [1,1,2,4,5,5,4,5,1,5]
        element = 5

        get_occurence(array1, element)

    except exception:
        logger.error("Invalid")
    
    