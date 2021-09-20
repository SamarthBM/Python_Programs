'''
* @Author: Samarth BM.
* @Date: 2021-09-20 14:32  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-20 14:32
* @Title: To lower case the first n characters in string. 
'''

from LogHandler import logger

def lowercase_to_range():
    """
    Description:
        This function is to lower case the first n characters in string.
    """
    try:
        
        string = "SAMARTH"
        n = int(input(" The string is {}, enter a range to lowercase: ".format(string)))
        print("After changing:", string[:n].lower()+ string[n:])
        logger.info("Changed the string")
        
    except Exception:
        logger.error("Invalid Input")

if __name__ == "__main__":
    lowercase_to_range()