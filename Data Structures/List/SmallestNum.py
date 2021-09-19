'''
* @Author: Samarth BM.
* @Date: 2021-09-19 13:53  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-19 13:53
* @Title: To get smallest number in a list.
'''

from LogHandler import logger

def get_smallest():
    """
    Description: 
        This function is to get smallest number in a list.
    """
    try:
        my_list = [2, 5, 6, 10, 1,  20, 14, 18]

        print("Smallest number in list is:", min(my_list))
        logger.info("Smallest number found")

    except Exception:
        logger.error("Invalid")

if __name__ == "__main__":
    get_smallest()       