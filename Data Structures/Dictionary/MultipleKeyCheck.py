'''
* @Author: Samarth BM.
* @Date: 2021-09-18 20:46  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-18 20:46
* @Title: To check for multiple keys in dictionary.
'''

from LogHandler import logger

def multiple_keys_check():
    """
    Description:
        This function is to check whether multiple keys exists in a dictionary.
    """

    dictionary = {
    'country': 'India',
    'state': 'karnataka',
    'zip': '577004'
    }
    
    print(dictionary.keys() >= {'country', 'state'})
    print(dictionary.keys() >= {'country', 'Place'})
    print(dictionary.keys() >= {'zip'})

if __name__ == "__main__":
    multiple_keys_check()