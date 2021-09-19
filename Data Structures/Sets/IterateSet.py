'''
* @Author: Samarth BM.
* @Date: 2021-09-19 11:56  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-19 11:56
* @Title: To iterate a set.
'''

from LogHandler import logger

def iterate_set():
    """
    Description: 
        This function is to create a set and iterate to get each values..
    """
    try:
        my_set = set([18, 'July', 'Samarth BM'])

        for val in my_set:
            print(val)
        logger.info("Inividual values in set printed")

    except Exception:
        logger.error("Invalid")

if __name__ == "__main__":
    iterate_set()