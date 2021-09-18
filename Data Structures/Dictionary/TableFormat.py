'''
* @Author: Samarth BM.
* @Date: 2021-09-18 19:28  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-18 19:28
* @Title: To print the dictionary in table format.
'''

from LogHandler import logger

def table_format():
    """
    Description:
        This function is to print a dictionary in table format.
    """
    
    try:

        dict1 = {
                1: ["Samarth", 23, 'Data Engineering'],
	            2: ["Jayanand", 24, 'Full stack'],
	            3: ["Karthik", 22, 'Python'],
	            }

        print("{:<10} {:<10} {:<10}".format('NAME', 'AGE', 'COURSE'))

        for key, value in dict1.items():
	        name, age, course = value
	        print("{:<10} {:<10} {:<10}".format(name, age, course))
        logger.info("Table format printed")
    
    except Exception:
        logger.error("Invalid Input")

if __name__ == "__main__":
    table_format()