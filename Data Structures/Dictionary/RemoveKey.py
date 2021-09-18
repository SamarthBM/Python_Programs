'''
* @Author: Samarth BM.
* @Date: 2021-09-18 13:39  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-18 13:39
* @Title: To remove a key in dictionary .
'''

from LogHandler import logger

def remove_key():
    """
    Description:
        This function is to remove a key from dictionary

    """
    try:

    
        countryAndSports = {
                            'India': 'Hockey',
                            'England' : 'Cricket',
                            'France' : 'Football',
                            }
    
        print("Before deleting: ",countryAndSports)

        if 'France' in countryAndSports:
            del countryAndSports['France']
            print("After deleting: ", countryAndSports)
            logger.info("Delete successful")

    except Exception:
        logger.error("Invalid")

if __name__ == "__main__":
    remove_key()