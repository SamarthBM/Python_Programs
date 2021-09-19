'''
* @Author: Samarth BM.
* @Date: 2021-09-19 14:22  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-19 14:22
* @Title: To remove duplicate value from the list.
'''

from LogHandler import logger

def remove_duplicant():
    """
    Description: 
        This function is to remove duplicate value from the list.
    """
    
    try:
        my_list = [1,2,3,2,5,1,9,14]
        print("Original list: ", my_list)

        final_list = list(set(my_list)) 
        print("After removing duplicate values: ", final_list)
        logger.info("Duplicate values removed")

    except Exception:
        logger.error("Invalid")

if __name__ == "__main__":
    remove_duplicant()