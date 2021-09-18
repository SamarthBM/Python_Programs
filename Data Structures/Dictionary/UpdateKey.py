'''
* @Author: Samarth BM.
* @Date: 2021-09-18 12:45  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-18 12:45
* @Title: To add key and value to existing dictionary.
'''

from typing import Dict
from LogHandler import logger

def update_key():
    """
    Description:
        This function is to update key to dictionary.
    """

    try:
        my_dict = {
                0: 10,
                1: 20,
               }

        print("Before adding key: ", my_dict)

        my_dict.update({2: 30})
        print("After adding key: ", my_dict)

        logger.info("Key added")

    except Exception:
        logger.error("Invalid Input")

if __name__ == "__main__":
    update_key()