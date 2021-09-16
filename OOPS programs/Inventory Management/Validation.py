from LogHandler import logger
import re

class Vaidation:
    """
    Description:
        This class holds the methods to validate inventory details using regex.
        Validation is done for Id, Name, price and weight.

    """    

    def validate_id():
        """
        Description:
            This function is to validate ID of the inventory.
            ID should start from number 1.

        Returns: Valid ID
            
        """
        try:        

            while True:
                id = input("Enter a unique id: ")
                if re.match("^[1-9][0-9]{1,}$", id):
                    return id
                else:
                    logger.error("Invalid id")

        except ValueError:
            logger.error("Invalid id")

    def validate_name():
        """
        Description:
            This function is to validate name of the inventory.
            Name should start with capital letter and should have minimum 3 letters.

        Returns: Valid inventory name.

        """
        try:

            while True:
                inv_name = input("Enter the name of inventory: ")
                if re.match("^[A-Z]{1}[a-z]{2,}$", inv_name):
                    return inv_name
                else:
                    logger.error("Invalid Input.")

        except ValueError:
            logger.error("Invalid Input")

    def valiadte_price():
        """
        Description:
            This function is to validate price of the inventory.

        Returns: Valid pice.

        """
        try:

            while True:
                price = input("Enter the price of inventory: ")
                if re.match("^[0-9]{1,}$", price):
                    return price
                else:
                    logger.error("Invalid input")

        except ValueError:
            logger.error("Invalid input")

    def validate_weight():
        """
        Description:
            This function is to validate weight of the inventory.

        Returns: Valid weight.

        """
        try:

            while True:
                weight = input("Enter the weight of inventory: ")
                if re.match("^[0-9]{1,}$", weight):
                    return weight
                else:
                    logger.error("Invalid input")

        except ValueError:
            logger.error("Invalid input")




