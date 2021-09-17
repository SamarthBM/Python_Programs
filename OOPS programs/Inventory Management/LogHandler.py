import logging

logger = logging

# Basic configuration and required format of the file.
logger.basicConfig(filename=r'E:\Python basics\OOPS programs\Inventory Management\Inventory management.log' , level=logging.INFO,
                    format='%(asctime)s:%(funcName)s:%(levelname)s:%(message)s' )

logger.basicConfig(filename=r'E:\Python basics\OOPS programs\Inventory Management\Inventory management.log' , level=logging.ERROR,
                    format='%(asctime)s:%(funcName)s:%(levelname)s:%(lineno)d')