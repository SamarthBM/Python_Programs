'''
* @Author: Samarth BM.
* @Date: 2021-09-19 18:38  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-19 18:38
* @Title: To return true if a common value is present in the two list.
'''

from LogHandler import logger

def common_data(list1, list2):
    """
    Description:
        This function is to return true if a common value is present in the two list.

    Parameter:
        list 1, list2 : Two lists to be compared .

    Return:
        True if common value is present in two list. 
    """

    try:
        for words1 in list1:
            for words2 in list2:
                if words1 == words2:
                    return True
    
    except Exception:
        logger.error("Invalid Input")

if __name__ == "__main__":

    list1 = [18,5,3,4,22,6]
    list2 = [9,22,7,15,9]

    if common_data(list1, list2):
        print("True")
    else:
        print("False")

