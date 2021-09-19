'''
* @Author: Samarth BM.
* @Date: 2021-09-19 12:18  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-19 12:18
* @Title: To remove a values from set if present. 
'''

from LogHandler import logger

def remove():
    """
    Description: 
        This function is to remove a value from set if present.
    """
    try:
        my_set = set([18, 'July', 'Samarth BM'])

        my_set.remove(19) # Logs an error if value not present.
        print(my_set)

    except Exception:
        logger.error("Value does not exist")

if __name__ == "__main__":
    remove()