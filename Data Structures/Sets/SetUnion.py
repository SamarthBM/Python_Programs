'''
* @Author: Samarth BM.
* @Date: 2021-09-19 12:35  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-19 12:35
* @Title: To create a union of sets. 
'''

from LogHandler import logger

def union():
    """
    Description:
        This function is to create union of sets.
    """
    try:
        
        set1 = set(["Cricket", "Football"])
        set2 = set(["Hockey", "Football"])
        print("Original set elements:")
        print(set1)
        print(set2)
        
        print("\nIntersection of two sets:")

        set_union = set1.union(set2)
        print(set_union)
        logger.info("Union set created")
    
    except Exception:
        logger.error("Invalid")

if __name__ == "__main__":
    union()