'''
* @Author: Samarth BM.
* @Date: 2021-09-20 13:01  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-20 13:01
* @Title: To find the length of string.
'''

from LogHandler import logger

def string_length():
    """
    Description: 
        This function is to find the length of string.
    """

    try:
        string = "samarth"
        print("The lenght of string is", len(string))
        logger.info("Length found")

    except Exception:
        logger.error("Invalid")

if __name__ == "__main__":
    string_length()