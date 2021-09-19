'''
* @Author: Samarth BM.
* @Date: 2021-09-19 18:27  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-19 18:27
* @Title: To find the words in list based om entered length of word.
'''

from LogHandler import logger

def find_word():
    """
    Description: 
        This function is to find the words in list based om entered length of word.
    """
    try:
        lenght = int(input("Enter the length of word to find: "))
        my_list = ['hey', 'there', 'my', 'name', 'is', 'samarth']
        new_list = []

        for words in my_list:
            if len(words) > lenght:
                new_list.append(words)
            else:
                print("Enter a proper length")
                break
            
        print("Word in list with length greater than {} are {}:".format(lenght, new_list))
        logger.info("New list with words created")

    except Exception:
        logger.error("Invalid")

if __name__ == "__main__":
    find_word()