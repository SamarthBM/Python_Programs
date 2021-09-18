'''
* @Author: Samarth BM.
* @Date: 2021-09-18 12:58  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-18 12:58
* @Title: To concatenate different dictionary to one dictionary.
'''

from LogHandler import logger

def concatenate():
    """
    Description: 
        This function is to concatenate different dictionaries to one dictionary.
    """

    try:

        dict1 = {
            0: 10,
            1: 20,
        }

        dict2 = {
            2: 30,
            3: 40
        }

        dict3 = {
            4: 50,
            5: 60
        }

        dict4 = {}

        for key_value in (dict1, dict2, dict3):
            dict4.update(key_value)

        print("Final dictionary is: ", dict4)
        logger.info("Concatenation success")
    
    except Exception:
        logger.error("Invalid Input")

if __name__ == "__main__":
    concatenate()