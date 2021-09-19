'''
* @Author: Samarth BM.
* @Date: 2021-09-19 12:10  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-19 12:110
* @Title: To remove values from set.
'''

from LogHandler import logger

def remove():
    """
    Description: 
        This function is to remove a value from set.
    """
    try:
        my_set = set([18, 'July', 'Samarth BM'])

        my_set.remove(18)
        print(my_set)

    except Exception:
        logger.error("Invalid")

if __name__ == "__main__":
    remove()