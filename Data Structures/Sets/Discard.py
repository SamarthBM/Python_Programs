'''
* @Author: Samarth BM.
* @Date: 2021-09-19 12:10  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-19 12:14
* @Title: To dicard a valuesfrom set.
'''

from LogHandler import logger

def discard():
    """
    Description: 
        This function is to dicard a value from set.
    """
    try:
        my_set = set([18, 'July', 'Samarth BM'])

        my_set.discard(18) # Does not show any error if element is not present.
        print(my_set)

    except Exception:
        logger.error("Invalid")

if __name__ == "__main__":
    discard()