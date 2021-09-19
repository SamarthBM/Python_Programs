'''
* @Author: Samarth BM.
* @Date: 2021-09-19 12:56  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-19 12:56
* @Title: To clear set.
'''

from LogHandler import logger

def clear_set():
    """
    Description: 
        This function is to clear set.
    """
    try:
        my_set = set([18, 'July', 'Samarth BM'])

        my_set.clear()
        logger.info("Set cleared")

    except Exception:
        logger.error("Invalid")

if __name__ == "__main__":
    clear_set()