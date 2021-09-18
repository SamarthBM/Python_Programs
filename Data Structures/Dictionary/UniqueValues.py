'''
* @Author: Samarth BM.
* @Date: 2021-09-18 18:50  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-18 18:50
* @Title: To print only the unique values in dictionary.
'''

from LogHandler import logger

def getUniqueDictionary():
    """
    Description:
        This function is to print only the unique values in dictionary.

    """
    try:

        dictionary = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
        print("Original List: ",dictionary)
        uniqueDict = set( val for dic in dictionary for val in dic.values())
        print("Unique Values: ",uniqueDict)
        logger.info("Unique values printed")

    except Exception:
        logger.error("Invalid")   

if __name__=="__main__":

    getUniqueDictionary()

    