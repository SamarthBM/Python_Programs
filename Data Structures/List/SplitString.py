'''
* @Author: Samarth BM.
* @Date: 2021-09-19 19:33  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-19 19:33
* @Title: To split the string in list.
'''

from LogHandler import logger

def split_string():
    """
        Description:
            This function is to split the string in list.
        """
    try:

        string = "samarth"
        my_list = list(string)

        print("Splitting string to list: ", my_list)
        logger.info("String splitted")

    except Exception:
        logger.error("Invalid Input")

if __name__ == "__main__":
    split_string()