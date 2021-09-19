'''
* @Author: Samarth BM.
* @Date: 2021-09-19 19:11  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-19 19:11
* @Title: To get the difference between two list.
'''

from LogHandler import logger

def get_difference():
        """
        Description:
            This function is to get the difference between two list.
        """
        try:
            list1 = [22, 14, 16, 18, 13]
            list2 = [11, 22, 13, 14]

            differenceList = list(set(list1) - set(list2)) +list(set(list2) - set(list1))

            print("Difference between two list is: ",differenceList)
            logger.info("Difference found")
        
        except Exception:
            logger.error("Inavlid input")

if __name__ == "__main__":
    get_difference()