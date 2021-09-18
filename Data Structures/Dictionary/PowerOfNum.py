'''
* @Author: Samarth BM.
* @Date: 2021-09-18 13:26  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-18 13:26
* @Title: To create dictionary with key and value is power of key.
'''

from LogHandler import logger

def powerOfNum():
    """
    Description:
        This function is to generate and print a dictionary that 
        contains a number (between 1 and n) in the form (x : x*x).
    """
    
    try:
        n = int(input("Enter a range: ")) 
        my_dict = dict()
        
        for num in range(1, n+1):
            my_dict[num]=num*num

        print(my_dict)
        logger.info("Dictionary created")

    except ValueError:
        logger.error("Invalid input")

if __name__ == "__main__":
    powerOfNum()