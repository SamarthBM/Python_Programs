'''
* @Author: Samarth BM.
* @Date: 2021-09-18 20:29  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-18 20:29
* @Title: To convert list into nested dictionary of key.
'''

from LogHandler import logger

def nested_dictionary():
    """
    Description:
        This function is to convert list into nested dictionary of keys.

    """
    num_list = [1, 2, 3, 4]
    nested_dict = current = {}
    
    for values in num_list:
        current[values] = {}
        current = current[values]
    
    print("Nested dictionary is: ", nested_dict)
    logger.info("Nested dictionary created")

if __name__ == "__main__":
    nested_dictionary()
