'''
* @Author: Samarth BM.
* @Date: 2021-09-19 23:11  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-19 23:11
* @Title: To create a tuple.
'''

from LogHandler import logger

def create_tuple():
    """
    Description: 
        This function is to create a tuple.
    """
    try:
        my_tuple = (18, 23, 17, 22, 8)
        print(my_tuple)


        logger.info("Tuple created")

    except Exception:
        logger.error("Invalid")

if __name__ == "__main__":
    create_tuple()