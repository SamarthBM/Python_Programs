'''
* @Author: Samarth BM.
* @Date: 2021-09-19 23:29  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-19 23:29
* @Title: To create a tuple colon.
'''

from LogHandler import logger
import copy

def tuple_colon():
    """
    Description: 
        This function is to create a tuple colon.
    """
    try:
        my_tuple = ("samarth", 23, "India", True, 18.88)
        new_tuple = copy.deepcopy(my_tuple)
        print(new_tuple)

        logger.info("Tuple colon created")

    except Exception:
        logger.error("Invalid")

if __name__ == "__main__":
    tuple_colon()