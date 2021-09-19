'''
* @Author: Samarth BM.
* @Date: 2021-09-20 00:01  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-20 00:01
* @Title: To remove an item from tuple.
'''

from typing import final
from LogHandler import logger

def remove():
    """
    Description: 
        This function is to remove an item from tuple.
        Tuple is first converted to list, after removing item 
        list is converted back to tuple.

    """
    try:
        
        my_tuple = ("samarth", 23, "India", 18)
        print("Original tuple:",my_tuple)
        
        convert_to_list = list(my_tuple) # Converting to list.
        convert_to_list.remove(18)

        final_tuple = tuple(convert_to_list) # Converting list to tuple again.
        print("Final tuple:",final_tuple)

        logger.info("Item deleted from tuple")

    except Exception:
        logger.error("Invalid")

if __name__ == "__main__":
    remove()