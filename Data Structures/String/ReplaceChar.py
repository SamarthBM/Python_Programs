'''
* @Author: Samarth BM.
* @Date: 2021-09-20 13:21  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-20 13:21
* @Title: To replace the occurence of first char in a string to $. 
'''

from LogHandler import logger

def replace_char():
    """
    Description:
        This function is to replace the occurence of first char in a string to $
    """

    try:
        
        string = "pipe"
        char = string[0]
        
        print("Before Replacing")
        print(string)
        
        new_string = string.replace(char, '$')
        new_string = char + new_string[1:]

        print("After Replacing")
        print(new_string)
        logger.info("Char replaced")

    except Exception:
        logger.error("Invalid input")

if __name__ == "__main__":
    replace_char()