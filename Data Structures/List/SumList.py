'''
* @Author: Samarth BM.
* @Date: 2021-09-19 13:42  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-19 13:42
* @Title: To add all values in a list.
'''

from LogHandler import logger

def add_list():
    """
    Description: 
        This function is to add all values in list.
    """
    try:
        my_list = [2, 5, 6, 10, 20, 14, 18]

        print("Sum of the list is:", sum(my_list))
        logger.info("Values added")

    except Exception:
        logger.error("Invalid")

if __name__ == "__main__":
    add_list()       