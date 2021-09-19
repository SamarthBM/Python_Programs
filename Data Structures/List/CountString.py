'''
* @Author: Samarth BM.
* @Date: 2021-09-19 14:01  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-19 14:01
* @Title: To count sting in list with lenght 2 or more and same first and last letter.
'''

from LogHandler import logger

def count_string():
    """
    Description: 
        This function is to count sting in list with lenght 2 or more 
        and same first and last letter.
    """
    
    try:
        string_list = (['abc', 'xyz', 'aba', '1221', 'pop'])
        count = 0

        for word in string_list:
            if len(word) > 1 and word[0] == word[-1]:
                count += 1
        print("Number of string with length more than 2 and same first and last letter is", count)
        logger.info("String count done")

    except Exception:
        logger.error("Invalid")

if __name__ == "__main__":
    count_string()