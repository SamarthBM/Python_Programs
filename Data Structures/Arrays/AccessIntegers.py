'''
* @Author: Samarth BM.
* @Date: 2021-09-17 20:48  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-17 20:48
* @Title: To create array of 5 integers and access them indivudually.
'''

from LogHandler import logger
import array as ar

def access_integer(arr):
    """
    Description:
        This function is to print the integers in array individually.

    Args:
        arr : Array to be accessed and displayed.
    """    

    try:

        for elements in range(len(arr)):
            print(arr[elements])

    except TypeError:
        logger.error("Invalid input")

if __name__ == "__main__":
    
    try:
        arr = ar.array("i", [18, 17, 22, 25, 40])
        access_integer(arr)

    except TypeError:
        logger.error("Invalid input")
