'''
* @Author: Samarth BM.
* @Date: 2021-09-19 14:11  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-19 14:11
* @Title: To print the list of tuple in increasing order keeping last value as key.
'''

from LogHandler import logger

def get_last_num(num):
    """
    Description:
        This function is to get the last number in the list of tuple.

    Args:
        num: Gets the last digit of num.

    Returns:
        Last digit of the tuple.
    """    
    return num[-1]

def sort():
    """
    Description: 
        This function is to print the list of tuple in increasing order keeping last value as key.
    """
    try:
        values = ([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)])
        print("Before sorting: ", values)

        sort_tuple = sorted(values, key=get_last_num)
        print("After sorting: ", sort_tuple)

        logger("Sorting done")

    except Exception:
        logger.error("Invalid")

if __name__ == "__main__":
    sort()