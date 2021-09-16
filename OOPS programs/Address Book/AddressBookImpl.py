"""
* @Author: Samarth BM.
* @Date: 2021-09-15 13:40  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-16 14:22 
* @Title: :To create a address book.
"""
import json
from logging import log

from LoggerFile import logger
from Validation import Validation

class AddressBookImpl:
    """
    Description:
        This class holds the methods to simulate the address book.
        Methods created: add_details, edit_details, remove_details and display.

    """    

    def __init__(self):
        self.address_book = []

    def open(self):       
        """
        Description:
            This function will open json file and get the details from json file.

        """        
        try:
            with open('E:\Python basics\OOPS programs\Address Book\AdressBook.json' , 'r') as file:
                self.address_book = json.load(file)

        except FileNotFoundError:
            logger.error("The file does not exists")

    def save(self):
        """
        Description:
            This function is to load the details into json file.
            The created list is dumped to this json file.

        """ 
        try:
            with open('E:\Python basics\OOPS programs\Address Book\AdressBook.json' , 'w+') as file:
                    json.dump(self.address_book, file, indent=2)
                    logger.info("File saved successflly")

        except Exception as e:
            logger.error(e)

        finally:
            file.close()

    def add_details(self):
        """
        Description:
            This function is to take user input from user for the contact details.
            If the details are valid then the entered details are saved to json file.

        """         

        details = {}

        id = Validation.validate_id()
        details['ID'] = id

        firstName = Validation.validate_first_name()
        details['firstName'] = firstName

        lastName = Validation.validate_last_name()
        details['lastName'] = lastName

        mobileNum = Validation.validate_mobile_number()
        details['mobile'] = mobileNum

        address = Validation.validate_address()
        details['address'] = address

        state = Validation.validate_state()
        details['state'] = state

        city = Validation.validate_city()
        details['city'] = city

        zip = Validation.validate_zip()
        details['zip'] = zip

        self.address_book.append(details) 
        self.save()

  
    def edit_details(self):
        """
        Description:
            This function is to edit the details of existing user.
            User is confirmed by checking ID.
            If ID exits then the details of user can be edited.

        """

        try: 
            if len(self.address_book) >= 1: # Checking if any contact details exists.
                id = input("Confirm Your id to edit the details: ")
                for i in range(len(self.address_book)): 
                    if (self.address_book[i]['ID'] == id): # Checking if entered id is present.                                          
                            option = int(input("Choose the following to edit\n 1 First Name \n 2 Last Name \n 3 Mobile Number\n 4 Address \n 5 State \n 6 city \n 7 Zip \n  "))
                            
                            if option == 1:
                                firstName = Validation.validate_first_name()
                                self.address_book[i]['firstName'] = firstName
                                self.save()
                                
                            elif option == 2:
                                lastName = Validation.validate_last_name()
                                self.address_book[i]['lastName'] = lastName
                                self.save()
                              
                            elif option == 3:
                                mobileNum = Validation.validate_mobile_number()
                                self.address_book[i]['mobile'] = mobileNum
                                self.save()
                                
                            elif option == 4:
                                address = Validation.validate_address()
                                self.address_book[i]['address'] = address
                                self.save()
                                
                            elif option == 5:
                                state = Validation.validate_state()
                                self.address_book[i]['state'] = state
                                self.save()
                                
                            elif option == 6:
                                city = Validation.validate_city()
                                self.address_book[i]['city'] = city
                                self.save()
                                
                            elif option == 7:
                                zip = Validation.validate_zip()
                                self.address_book[i]['zip'] = zip
                                self.save()

                            else:
                                print("Invalid Option")
                                self.edit_details()

                    else:
                        print("ID does not exists")                    
        except Exception as e:
            logger.error("Invalid input",e)        
            self.edit_details()    


    def remove_user(self):
        """
        Description:
            This function is to delete the contact details of user.
            ID of user is confirmed to delete the contact.

        """
        try:
            if len(self.address_book) >= 1: # Checking if any contact details exists.
                id = input("Confirm Your id to remove the details: ")
                for i in range(len(self.address_book)): 
                    if (self.address_book[i]['ID'] == id): # Checking if entered id is present.
                        del self.address_book[i]
                        self.save()

        except Exception as e:
            logger.error(e)

    def display_contact(self):
        """
        Description:
            This function is to display all contact details.

        """

        print(self.address_book)

        
           
                    





