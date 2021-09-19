'''
* @Author: Samarth BM.
* @Date: 2021-09-19 12:22  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-19 12:22
* @Title: To create a intersection of sets. 
'''

from LogHandler import logger

def intersection():
    """
    Description:
        This function is to create intersection of sets.
    """
    try:
        
        set1 = set(["Cricket", "Football"])
        set2 = set(["Hockey", "Football"])
        print("Original set elements:")
        print(set1)
        print(set2)
        
        print("\nIntersection of two sets:")

        set_intersection = set1.intersection(set2)
        print(set_intersection)
    
    except Exception:
        logger.error("Invalid")

if __name__ == "__main__":
    intersection()