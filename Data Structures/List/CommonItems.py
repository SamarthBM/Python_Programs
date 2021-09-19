'''
* @Author: Samarth BM.
* @Date: 2021-09-19 19:22  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-19 19:22
* @Title: To get common items from two list.
'''

from LogHandler import logger

def common_item():
    """
    Description:
        This function is to get common items from two list.

    """
    try:
        
        list1 = ['s', 'a', 'm', 'a', 'r', 't', 'h']
        list2 = ['s', 'a', 'm']
        final_list = []

        for val1 in list1:
            for val2 in list2:
                if val1 == val2:
                    final_list.append(val1)
            
        print(final_list)
    
    except Exception:
        logger.error("Invalid Input")

if __name__ == "__main__":
    common_item()

   



