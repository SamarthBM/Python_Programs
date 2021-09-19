'''
* @Author: Samarth BM.
* @Date: 2021-09-19 18:08  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-19 18:08
* @Title: To copy one list to another list.
'''

from LogHandler import logger

def copy_list():
    """
    Description: 
        This function is to copy one list to another list.
    """
    try:
        my_list = [1,2,3,2,5,1,9,14]
        new_list = list(my_list)

        print("New list is: ", new_list)
        logger.info("List copied to another list")

    except Exception:
        logger.error("Invalid")

if __name__ == "__main__":
    copy_list()