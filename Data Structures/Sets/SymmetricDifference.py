'''
* @Author: Samarth BM.
* @Date: 2021-09-19 12:47  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-19 12:47
* @Title: To create a symmetric difference of sets. 
'''

from LogHandler import logger

def symmetric_difference():
    """
    Description:
        This function is to create a symmetric difference of sets.
    """
    try:
        
        set1 = set(["Cricket", "Football", "TT"])
        set2 = set(["Hockey", "Football", "Cricket"])
        print("Original set elements:")
        print(set1)
        print(set2)
        
        print("\n symmetric difference between set 1 and 2: ")
        symmetric_diff = set1.symmetric_difference(set2)
        print(symmetric_diff)
    
        logger.info("symmetric set difference printed")
    
    except Exception:
        logger.error("Invalid")

if __name__ == "__main__":
    symmetric_difference()