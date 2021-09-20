'''
* @Author: Samarth BM.
* @Date: 2021-09-20 13:44  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-20 13:44
* @Title: To take a user input for string and display it in upper and lower case. 
'''

from LogHandler import logger

try:
    
    string = input("Enter the String: ")

    print("Entered string in upper case",string.upper())
    print("Entered string in lower case",string.lower())

except Exception:
    logger.error("Invalid Input")