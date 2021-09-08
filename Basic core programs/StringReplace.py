'''
* @Author: Samarth BM.
* @Date: 2021-09-08 19:36  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-08 19:46
* @Title: User Input and Replace String Template “Hello <<UserName>>, How are you?”
'''

str = "Hello <<UserName>>, How are you?"

# Userinput for the name.
name = input("Please enter your name: ")

# Checking if length of name is greater or equal to 3.
if len(name) >=3:
    new_str = str.replace('<<UserName>>', name )
    print(new_str)
else:
    print("Enter a valid name")

