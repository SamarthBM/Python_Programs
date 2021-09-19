'''
* @Author: Samarth BM.
* @Date: 2021-09-19 23:22  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-19 23:22
* @Title: To create a tuple and unpack values to variables.
'''

from LogHandler import logger

def unpack_tuple():
    """
    Description: 
        This function is to create a tuple and unpack values to variables.
    """
    try:
        my_tuple = ("samarth", 23, "India")
        name, age, country = my_tuple

        print(name)
        print(age)
        print(country)

        logger.info("Tuple unpacked")

    except Exception:
        logger.error("Invalid")

if __name__ == "__main__":
    unpack_tuple()