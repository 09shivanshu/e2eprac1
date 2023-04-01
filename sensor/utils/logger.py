import logging
import os
from datetime import datetime

#log file name
LOG_FILE_NAME = "f{datetime.now().strftime(%m%d%y__%h%m%s)}.log"
# log directory
LOG_FILE_DIR = os.path.join(os.getcwd(),"logs")

#create folder if not availble
os.makedirs(LOG_FILE_DIR,exist_ok=True)

#log file path
logging.basicConfig(
    filename = LOG_FILE_PATH,
    format = "[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO,
)