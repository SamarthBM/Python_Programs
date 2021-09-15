"""
* @Author: Samarth BM.
* @Date: 2021-09-15 13:40  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-15 13:40 
* @Title: :To create a address book.
"""

from LoggerFile import logger
from AddressBookImpl import AddressBookImpl

if __name__ == "__main__":
    try:
       
        while True:
            address = AddressBookImpl()
            choose = int(input("Choose what you want to do: \n 1. Open existing.\n 2. Add new.\n 3. Exit\n "))

            if choose == 1:
                address.open()
                choose1 = int(input("Choose what you want to do: \n1. Add details\n2. Edit details\n3. Delete contact\n4. Display\n"))
                if choose1 == 1:
                    address.add_details()
                    logger.info(" Data Added Successfully ")

                elif choose1 == 2:
                    address.edit_details()
                    logger.info("Edited successfully")

                elif choose1 == 3:
                    address.remove_user()
                    logger.info("Deleted successfully")

                elif choose1 == 4:
                    address.display_contact()

            elif choose == 2:
                address.add_details()
            elif choose == 3:
                exit()
        
                
    except ValueError:
        logger.error("Invalid input")
