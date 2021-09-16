"""
* @Author: Samarth BM.
* @Date: 2021-09-16 10:35  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-16 10:35 
* @Title: :To simulate inventory management program.
"""

from LogHandler import logger
from InventoryManagementImpl import InventoryManagementImpl

if __name__ == "__main__":
    try:
        while True:
            inventory_management = InventoryManagementImpl()
            choose = int(input("Choose what you want to do\n1.Open existing inventory\n2.Add new inventory.\n3.Exit\n"))

            if choose == 1:
                inventory_management.open()
                choose1 = int(input("Enter what you want to do\n1.Add inventory.\n2.Edit inventory.\n3.Delete\n4.Display\n"))
                if choose1 == 1:
                    inventory_management.add()
                    logger.info("Inventory Aadded successfuly")

                elif choose1 == 2:
                    inventory_management.edit()
                    logger.info("Inventory edited successfully")

                elif choose1 == 3:
                    inventory_management.remove()
                    logger.info("Deleted successfully")

                elif choose1 == 4:
                    inventory_management.display()

            elif choose == 2:
                inventory_management.add()
            
            elif choose == 3:
                exit()
    

    except ValueError:
        logger.error("Enter valid input")