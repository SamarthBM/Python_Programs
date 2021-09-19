'''
* @Author: Samarth BM.
* @Date: 2021-09-19 12:40  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-19 12:40
* @Title: To create a set difference. 
'''

from LogHandler import logger

def set_difference():
    """
    Description:
        This function is to create a set difference.
    """
    try:
        
        set1 = set(["Cricket", "Football"])
        set2 = set(["Hockey", "Football"])
        print("Original set elements:")
        print(set1)
        print(set2)
        
        print("\n Difference between set 1 and 2: ")
        set_diff1 = set1.difference(set2)
        print(set_diff1)

        print("\n Difference between set 2 and 1: ")
        set_diff2 = set2.difference(set1)
        print(set_diff2)

        logger.info("Set difference printed")
    
    except Exception:
        logger.error("Invalid")

if __name__ == "__main__":
    set_difference()