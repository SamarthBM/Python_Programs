'''
* @Author: Samarth BM.
* @Date: 2021-09-18 12:25  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-18 12:25
* @Title: To sort a dictionary in ascending and descending order by value.
'''

from LogHandler import logger

def ascending_sort(my_dict ):
    """
    Description:
        This function is to sort the dictionary values in ascending order.

    Args:
        my_dict: Dictionary to be sorted.
    """    
    try:       
        ascending = sorted(my_dict.values())
        print("Sorting the dictionary in ascending order by value: ",ascending)
        logger.info("Dictionary sorted in ascending order.")

    except Exception:
        logger.error("Inavlid")


def descending_sort(my_dict):
    """
    Description:
        This function is to sort the dictionary values in descending order.

    Args:
        my_dict: Dictionary to be sorted.
    """
    try:
        descending = sorted(my_dict.values(), reverse=True)
        print("Sorting the dictionary in descending order by value: ",descending)
        logger.info("Dictionary sorted in descending order.")

    except Exception:
        logger.error("Inavlid")


if __name__ == "__main__":
    try:
        my_dict = {'a' : 5, 'b' : 7, 'c' : 1, 'd' : 9, 'e' : 4}
        ascending_sort(my_dict)
        descending_sort(my_dict)

    except Exception:
        logger.error("Inavlid")