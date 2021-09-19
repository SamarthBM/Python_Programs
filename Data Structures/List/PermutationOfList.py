'''
* @Author: Samarth BM.
* @Date: 2021-09-19 19:02  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-19 19:02
* @Title: To generate all permutation of list.
'''

from LogHandler import logger
from itertools import permutations

def permutation_list():
    """
    Description: 
        This function is to generate all permutation of list.
    """
    try:

        list1 = [4, 5, 6]
        list2 = list(permutations(list1))
        print(list2)
        logger.info("Permutation done")

    except Exception:
        logger.error("Inavlid input")

if __name__ == "__main__":
    permutation_list()