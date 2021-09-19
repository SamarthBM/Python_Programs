'''
* @Author: Samarth BM.
* @Date: 2021-09-20 00:26  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-20 00:26
* @Title: To reverse a tuple.
'''

from LogHandler import logger

def reverse():
    """
    Description: 
        This function is to reverse a tuple.
    """
    try:
        my_tuple = ("Im reversing this")
        new_tuple = reversed(my_tuple)
        print(tuple(new_tuple))
        logger.info("Tuple reversed")

    except Exception:
        logger.error("Invalid input")

if __name__ == "__main__":
    reverse()