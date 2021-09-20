'''
* @Author: Samarth BM.
* @Date: 2021-09-20 13:11  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-20 13:11
* @Title: To count characters in a string.
'''

from LogHandler import logger

def char_count():
    """
    Description:
        This function is to count characters in a string.
    """
    try:

        string = "samarth"
        charFrequency = {}
        
        for char in string:
            if char in charFrequency:
                charFrequency[char] += 1
            else:
                charFrequency[char] = 1

        print(charFrequency)

    except Exception:
        logger.error("Invalid")

if __name__ == "__main__":
    char_count()
