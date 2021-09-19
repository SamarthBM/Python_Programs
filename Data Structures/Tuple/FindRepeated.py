'''
* @Author: Samarth BM.
* @Date: 2021-09-19 23:31  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-19 23:31
* @Title: To create a tuple and count the repeated element.
'''

from LogHandler import logger

def count():
    """
    Description: 
        This function is to  create a tuple and count the repeated element.
    """
    
    try:
        my_tuple = (18, 12, 2, 2, 1, 5, 18, 17, 18, 2)
        find = int(input("Enter number to find its count: "))
        count_element = my_tuple.count(find)
        print("Element {} has been repeated for {} times.".format(find,count_element))
        logger.info("Element count found")

    except Exception:
        logger.error("Invalid input")

if __name__ == "__main__":
    count()