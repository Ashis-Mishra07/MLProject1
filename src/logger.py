# The only purpose is to log the changes that goes on the file to store the changes that occur .

import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"   # this will create the logs file with the current date and time .
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)  # to fetch the path where the logs are made
os.makedirs(logs_path, exist_ok=True)   # this means even though it is present , append it to the file .

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)  

logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
)


