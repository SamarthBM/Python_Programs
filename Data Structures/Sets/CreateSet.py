'''
* @Author: Samarth BM.
* @Date: 2021-09-19 11:47  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-19 11:47
* @Title: To create a set.
'''

from LogHandler import logger

def create_set():
    """
    Description: 
        This function is to  create a set.
    """
    
    try:
        my_set = set([18, 'July', 'Samarth BM', 18])
        print("Set created using set() constructor" , my_set)
        
        next_set = {18, 'July', 'samarth', 18}
        print("Set created by typing within curly brackets" , next_set)

        logger.info("Set created")

    except Exception:
        logger.error("Invalid")

if __name__ == "__main__":
    create_set()