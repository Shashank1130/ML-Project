# We will use to log 

# logger is for the purpose that any execution that probably happens we should be able to log all those information, the execution everything in some files so that we will able to track if there is some errors even the custom exception error we will try to log that into the text file, for that also we have to implement logger.

import logging
import sys
import os
from datetime import datetime

LOG_FILE =f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO,
)


