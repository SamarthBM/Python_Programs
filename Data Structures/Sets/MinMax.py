'''
* @Author: Samarth BM.
* @Date: 2021-09-19 13:10  
* @Last Modified by: Samarth BM.
* @Last Modified time: 2021-09-19 13:10
* @Title: To print minimum and maximum number in a set.
'''

from LogHandler import logger

def min_max():
    """
    Description: 
        This function is to find minimum and maximum number in a set.
    """
    try:
        my_set = {5, 2, 9, 44, 12, 124, 18, 5, 123}

        print("Maximum number is: ", max(my_set))
        print("Minimum number is: ", min(my_set))
        
        logger.info("Maximum and minimum number found")

    except Exception:
        logger.error("Error")

if __name__ == "__main__":
    min_max()