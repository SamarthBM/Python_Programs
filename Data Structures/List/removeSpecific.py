'''
* @Author: Samarth BM.
* @Date: 2021-09-19 18:50  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-19 18:50
* @Title: To remove elements in a list using index number.
'''

from LogHandler import logger

def remove_specific():
    """
    Description: 
        This function is to remove elements in a list using index number.
    """
    try:
        my_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

        my_list.pop(0)
        my_list.pop(3)
        my_list.pop(3)
    
        print("List after deleting: ",my_list)
        logger.info("Elements deleted")

    except Exception:
        logger.error("Invalid Input")

if __name__ == "__main__":
    remove_specific()