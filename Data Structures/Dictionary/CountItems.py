'''
* @Author: Samarth BM.
* @Date: 2021-09-18 21:01  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-18 21:01
* @Title: To count number of items in dictionary.
'''

def count_items():
    """
    Description:
        This function is to count number of items in dictionary

    """

    dictionary = {
        'country': 'India',
        'state': 'karnataka',
        'zip': '577004',
        }

    print("Number of items in dictionary is:",len(dictionary.items()))

if __name__ == "__main__":

    count_items()