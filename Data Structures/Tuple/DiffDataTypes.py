'''
* @Author: Samarth BM.
* @Date: 2021-09-19 23:15  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-19 23:15
* @Title: To create a tuple with different data types.
'''

from LogHandler import logger

def tuple():
    """
    Description: 
        This function is to create a tuple with different data types.
    """
    try:
        my_tuple = ("samarth", 23, "India", True, 18.88)
        print(my_tuple)

        logger.info("Tuple created")

    except Exception:
        logger.error("Invalid")

if __name__ == "__main__":
    tuple()