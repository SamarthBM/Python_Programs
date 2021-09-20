'''
* @Author: Samarth BM.
* @Date: 2021-09-20 13:55  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-20 13:55
* @Title: To write a program that accepts a comma separated sequence of words as input
          and prints the unique words in sorted form (alphanumerically). 
'''

from LogHandler import logger

def sort():
    """
    Description:
        This function is to sort the comma separated value.
    """
    try:

        items = 'java,python,nodejs,react,python'
        words = [word for word in items.split(",")]
        print(":".join(sorted(list(set(words)))))
    
    except Exception:
        logger.error("Invalid Input")

if __name__ == "__main__":
    sort()