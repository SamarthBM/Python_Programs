'''
* @Author: Samarth BM.
* @Date: 2021-09-20 14:20  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-20 14:20
* @Title: To count the occurence in a string. 
'''

from LogHandler import logger

def occurence_count():
    """
    Description:
        This function is to count the occurence in a string.
    """
    try:
        
        string = "Hi there how are you, is there anything to talk?"
        search = input("Enter a word to search: ")
        print("The word {} has appeared for {} times.".format(search,string.count(search)))

    except Exception:
        logger.error("Invalid Input")

if __name__ == "__main__":
    occurence_count()