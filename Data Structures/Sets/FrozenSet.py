'''
* @Author: Samarth BM.
* @Date: 2021-09-19 13:01  
* @Last Modified by: Samarth BM.
* @Last Modified time: 2021-09-19 13:01
* @Title: To create a frozen set.
'''

from LogHandler import logger

def frozen_set():
    """
    Description: 
        This function is to create a frozen set.
    """
    try:
        my_set = set([18, 'July', 'Samarth BM'])

        f_set = frozenset(my_set)
        print(f_set)
        logger.info("Frozen set created")

    except Exception:
        logger.error("Invalid")

if __name__ == "__main__":
    frozen_set()