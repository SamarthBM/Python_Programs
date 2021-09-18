'''
* @Author: Samarth BM.
* @Date: 2021-09-18 19:43  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-18 19:43
* @Title: To count the values in a dictionary.
'''

from LogHandler import logger

def count_values():
    """
    Description: 
        This function is to  count the values associated with key.
    """
    try:

        student = [{'id': 1, 'success': True, 'name': 'Lary'},
                   {'id': 2, 'success': False, 'name': 'Rabi'},
                   {'id': 3, 'success': True, 'name': 'Alex'}]
    
        print("Number of True is:", sum(d['success'] for d in student))

    except Exception:
        logger.error("Invalid")

if __name__ == "__main__":
    count_values()