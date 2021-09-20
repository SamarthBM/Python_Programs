'''
* @Author: Samarth BM.
* @Date: 2021-09-20 13:44  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-20 13:44
* @Title: To find the longest string. 
'''

from LogHandler import logger

def longest_string():
    """
    Description:
        This function is to find the longest string.
    """
    try:

        stringList = ["Samarth", "Rahul", "piku"]
        longest_word = []

        for string in stringList:
            temp = longest_word.append(len(string))
        temp1 = longest_word.sort()
        print("Longest word is:",longest_word[-1])
        logger.info("Longest string found")

    except Exception:
        logger.error("Invalid input")

if __name__ == "__main__":
    longest_string()