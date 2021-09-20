'''
* @Author: Samarth BM.
* @Date: 2021-09-20 14:10  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-20 14:10
* @Title: To split a string. 
'''

from LogHandler import logger

def split_string():
    """
    Description:
        This function is to split a string.
    """
    try:
        
        string = 'https://www.w3resource.com/python-exercises/string'
        print(string.rsplit('/', 1)[0])
        print(string.rsplit('-', 1)[0])

    except Exception:
        logger.error("Invalid Input")

if __name__ == "__main__":
    split_string()