# We will use this file for exception handling

"""
    # sys module:

        The python sys module provides functions and variables which are used to manipulate different parts of the Python Runtime Environment. It lets us access system-specific parameters and functions.
"""

import sys
from src.logger import logging


def error_message_detail(error, error_detail: sys):
    """
    # exc_info():- execution info, will give us 3 imp info

        # exc_tb = this varible will give us all the information like 'on which file the exception has occured', 'on which line number the exception has occured', all thise infoemation will be probably given and will be stored in this particular variable

    """
    _, _, exc_tb = error_detail.exc_info()
    filename =exc_tb.tb_frame.f_code.co_filename # search for 'custom exception handling in python documentation'
    error_message = "Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
        filename, 
        exc_tb.tb_lineno, 
        str(error))

    return error_message
    
    # lineno-> line number 


# overwrtiting the __init__ and __str__ methods
class CustomException(Exception):
    def __init__(self, error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message
    

if __name__ == "__main__":

    try:
        a=1/0
    except Exception as e:
        logging.info("Divide by zero")
        raise CustomException(e,sys)


