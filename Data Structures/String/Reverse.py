'''
* @Author: Samarth BM.
* @Date: 2021-09-20 14:26  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-20 14:26
* @Title: To reverse a string. 
'''

from LogHandler import logger

def reverse():
    """
    Description:
        This function is to reverse a string.
    """
    try:
        
        string = "samarth"
        print("String before reversing:", string)
        print("String after reversing:",string[-1::-1])
        logger.info("String reversed")
        
    except Exception:
        logger.error("Invalid Input")

if __name__ == "__main__":
    reverse()