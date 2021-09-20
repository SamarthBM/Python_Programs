'''
* @Author: Samarth BM.
* @Date: 2021-09-20 13:28  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-20 13:28
* @Title: To add 'ing' to string, if ing present then add 'ly'. 
'''

from LogHandler import logger

def add(str):
    """
    Description:
        This function is to add 'ing' to string, if ing present then add 'ly'.
    Parameter:
        str: String to which ing or ly to be added.
    Returns:
        changed string.
    """

    if len(str) > 2:
        if str[-3:] == 'ing':
            str += 'ly'
        else:
            str += 'ing'
    return str

if __name__ == "__main__":

    try:

        print(add('collection'))
        print(add('add'))
        print(add('string'))
        print(add('ab'))

    except Exception:
            logger.error("Invalid Input")