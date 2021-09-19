'''
* @Author: Samarth BM.
* @Date: 2021-09-20 00:12  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-20 00:12
* @Title: To slice a tuple.
'''

from LogHandler import logger

def slice_tuple():
    """
    Description: 
        This function is to perform slicing in tuple.
    """
    try:

        tuple = (10,20,30,40,50,60,70,80,90,100)

        print(tuple[1:]) # slicing starts from 1 to end

        print(tuple[:5]) # slicing starts from 0 and ends at 5th index
        
        print(tuple[1:4]) # slicing from 1 to 4 

        print(tuple[::2]) # slicing from start to end using step sizes of 2

        print(tuple[-1::-1]) # Slicing from end to start.

    except Exception:
        logger.error("Invalid input")

if __name__ == "__main__":
    slice_tuple()