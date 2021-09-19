'''
* @Author: Samarth BM.
* @Date: 2021-09-19 23:40  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-19 23:40
* @Title: To find a element in tuple.
'''

from LogHandler import logger

def find_element():
    """
    Description: 
        This function is to find a element in tuple.
    """

    try:
        my_tuple = (18, 12, 2, 2, 1, 5, 18, 17, 18, 2)
        find = int(input("Enter number to find: "))
        print(find in my_tuple)
        logger.info("Element checked")

    except Exception:
        logger.error("Invalid input")

if __name__ == "__main__":
    find_element()