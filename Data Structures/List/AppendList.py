'''
* @Author: Samarth BM.
* @Date: 2021-09-19 19:20  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-19 19:20
* @Title: To append one list to another list.
'''

from LogHandler import logger

def append_list():
        """
        Description:
            This function is to append one list to another list.
        """
        try:
            list1 = [22, 14, 16, 18, 13]
            list2 = [11, 22, 13, 14]

            final_list = list1 + list2

            print("Final list is: ",final_list)
            logger.info("List appended")
        
        except Exception:
            logger.error("Inavlid input")

if __name__ == "__main__":
    append_list()