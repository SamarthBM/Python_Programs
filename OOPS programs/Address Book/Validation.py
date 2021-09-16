from LoggerFile import logger
import re 

class Validation:
    """
    Description:
        This class holds the methods to validate all the details entered by User.
        Regex is used to validate the details.

    """    

    def validate_id():
        """
        Description:
            This function is to validate ID of the person.
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

    def validate_first_name():
        """
        Description:
            This function is to validate first name of the person.
            Name should start with capital letter and should have minimum 3 letters.

        Returns: Valid first name.
            
        """
        try:

            while True:
                firstName = input("Enter your first name: ")
                if re.match("^[A-Z]{1}[a-z]{2,}$", firstName):
                    return firstName
                else:
                    logger.error("Invalid first name.")

        except ValueError:
            logger.error("Invalid First name")

    def validate_last_name():
        """
        Description:
            This function is to validate last name of the person.
            Last name should start with capital letter and should have minimum 2 letters.

        Returns: Valid last name.
            
        """
        try:

            while True:
                lastName = input("Enter your last name: ")
                if re.match("^[A-Z]{1}[a-z]{1,}$", lastName):
                    return lastName
                else:
                    logger.error("Invalid last name.")

        except ValueError:
            logger.error("Invalid Last name")

    def validate_mobile_number():
        """
        Description:
            This function is to validate mobile number of the person.
            Mobile number should start with country code 91 and should have 10 digits.

        Returns: Valid mobile number.
            
        """
        try:

            while True:
                mobileNum = input("Enter your mobile number: ")
                if re.match("^(91)[0-9]{10}$",  mobileNum):
                    return mobileNum
                else:
                    logger.error("Invalid mobile number")

        except ValueError:
            logger.error("Invalid mobile number")

    def validate_address():
        """
        Description:
            This function is to validate address of the person.
            Address can have upper and lower case and numeric values.

        Returns: Valid address.
            
        """

        try:
            while True:

                address = input("Enter your address: ")
                if re.match("^[A-za-z0-9]*$", address):
                    return address
                else:
                    logger.error("Invalid address")

        except ValueError:
            logger.error("Invalid adress")

    def validate_state():
        """
        Description:
            This function is to validate entered state of the person.

        Returns: Valid State.
            
        """
        try:

            while True:
                state = input("Enter your state: ")
                if re.match("^[A-Z]{1}[a-z]{2,}$", state):
                    return state
                else:
                    logger.error("Invalid state")

        except ValueError:
            logger.error("Invalid state")

    def validate_city():
        """
        Description:
            This function is to validate entered city of the person.

        Returns: Valid city.
            
        """
        try:
            
            while True:
                city = input("Enter your city: ")
                if re.match("^[A-Z]{1}[a-z]{2,}$", city):
                    return city
                else:
                    logger.error("Invalid city")

        except ValueError:
            logger.error("Invalid city")

    def validate_zip():
        """
        Description:
            This function is to validate entered Zip code of the person's city.

        Returns: Valid zip code.
            
        """

        try:
            while True:
                zip = input("Enter your zip: ")
                if re.match("^[1-9]{1}[0-9]{5}$", zip):
                    return zip
                else:
                    logger.error("Invalid zip")

        except ValueError:
            logger.error("Invalid zip")
    


