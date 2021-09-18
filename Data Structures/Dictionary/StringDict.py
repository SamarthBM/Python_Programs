'''
* @Author: Samarth BM.
* @Date: 2021-09-18 19:17  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-18 19:17
* @Title: To create a dictionay from string and counting its letters.
'''

from LogHandler import logger

def create_dict():
    """
    Description:
        This function is to create a dictionary from a string.
    """
    
    try:
        str1 = 'w3resource' 
        my_dictionary = {}
        
        for letter in str1:
            my_dictionary[letter] = my_dictionary.get(letter, 0) + 1
        
        print(my_dictionary)
        logger.info("Dictionary created")

    except Exception:
        logger.error("Invalid")

if __name__ == "__main__":
    
    create_dict()
