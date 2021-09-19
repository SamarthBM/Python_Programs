'''
* @Author: Samarth BM.
* @Date: 2021-09-19 23:49  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-19 23:49
* @Title: To convert list to tuple.
'''

from LogHandler import logger

def List_to_tuple():
    """
    Description: 
        This function is to convert list to tuple.
    """
    try:

        my_list = ["samarth", 23, "India"]
        print("List is:",my_list)
        
        my_tuple = tuple(my_list)
        print("After converting list to tuple:", my_tuple)

        logger.info("List converted to tuple")

    except Exception:
        logger.error("Invalid")

if __name__ == "__main__":
    List_to_tuple()