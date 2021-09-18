'''
* @Author: Samarth BM.
* @Date: 2021-09-18 13:11  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-18 13:11
* @Title: To iterate over a dictionary using for loop.
'''

from LogHandler import logger

def iterare_dict():

    """
    Description:
        This function is to iterate over dictionary using for loop
        to get keys and values, only keys and only values.
        
    """

    countryAndSports = {
                     'India': 'Hockey',
                     'England' : 'Cricket',
                     'France' : 'Football',
                    }
                      
  
    # To iterate and print key with values.
    print("Keys and values of the given dictionary are: ")
    for country, sport in countryAndSports.items():
        print(country, ":", sport)
    logger.info("Fetched keys and values")
    print()

    # To iterate and print keys.
    print("Keys of the given dictionary are: ")
    for keys in countryAndSports.keys():
        print(keys)
    logger.info("Fetched keys")
    print()

    # To iterate and print values.
    print("Values of the given dictionary are: ")
    for values in countryAndSports.values():
        print(values)
    logger.info("Fetched values")
    print()

if __name__ == "__main__":
    iterare_dict()