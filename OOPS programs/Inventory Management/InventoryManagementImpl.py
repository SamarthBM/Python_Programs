"""
* @Author: Samarth BM.
* @Date: 2021-09-16 10:35  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-16 10:35 
* @Title: :To simulate inventory management program.
"""

import json
from LogHandler import logger
from Validation import Vaidation

class InventoryManagementImpl:

    """
    Description:
        This class holds all the methods to simulate the inventory management and store details into json file.
        Methods created: Add, edit and remove.

    """
    def __init__(self):
        self.inventory = []

    def open(self):
        """
        Description:
            This function will open json file and get the details from json file.

        """    

        try:
            with open('E:\Python basics\OOPS programs\Inventory Management\Inventory.json' , 'r') as file:
                self.inventory = json.load(file)

        except FileNotFoundError:
            logger.error("The file does not exists")

    def save(self):
        """
        Description:
            This function is to load the details into json file.
            The created list is dumped to this json file.

        """ 
        try:
            with open('E:\Python basics\OOPS programs\Inventory Management\Inventory.json' , 'w+') as file:
                    json.dump(self.inventory, file, indent=2)
                    logger.info("File saved successflly")

        except Exception as e:
            logger.error(e)

        finally:
            file.close()

    def add(self):
        """
        Description:
            This function is to add inventory details into the json file.
            Details added are: id, name, price and weight.

        """        
        try:
            details = {}
            id = Vaidation.validate_id()
            details['Id'] = id

            inv_name = Vaidation.validate_name()
            details['name'] = inv_name

            price = Vaidation.valiadte_price()
            details['price'] = price

            weight = Vaidation.validate_weight()
            details['weight'] = weight

            self.inventory.append(details)
            self.save()

        except ValueError:
            logger.error("Enter valid input")

    def edit(self):
        """
        Description:
            This function is to edit the inventory details present in the json file.
            Price and weight can be edited.

        """        
        try:
            
            if len(self.inventory) >= 1:
                id = input("Enter id to edit: ")
                for i in range(len(self.inventory)):
                    if (self.inventory[i]['Id'] == id):
                        option = int(input("Choose what you want to edit\n1.Price.\n2.Weight.\n"))

                        if option == 1:
                            Price = Vaidation.valiadte_price()
                            self.inventory[i]['price'] = Price
                            self.save()

                        else: 
                            weight = Vaidation.validate_weight()
                            self.inventory[i]['weight'] = weight  
                            self.save()        

        except ValueError:
            logger.error("Invalid input")

    def remove(self):
        """
        Description:
            This function is to remove the inventory details present in the json file.

        """ 
        if len(self.inventory) >= 1:
                id = input("Enter id to delete: ")
                for i in range(len(self.inventory)):
                    if (self.inventory[i]['Id'] == id):
                        del self.inventory[i]
                        self.save()

    def display(self):
        """
        Description:
            This function is to display the list of inventory details.

        """

        print(self.inventory)


            

    

            
            
            





