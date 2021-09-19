'''
* @Author: Samarth BM.
* @Date: 2021-09-19 12:06  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-19 12:06
* @Title: To add values to existing set.
'''

from LogHandler import logger

def add():
    """
    Description: 
        This function is to add values to existing set.
    """
    try:
        my_set = set([18, 'July', 'Samarth BM'])

        my_set.add(23)
        my_set.add("Male")
        
        logger.info("Values added")
        print(my_set)

        for val in my_set:
            print(val)
        logger.info("Inividual values in set printed")

    except Exception:
        logger.error("Invalid")

if __name__ == "__main__":
    add()