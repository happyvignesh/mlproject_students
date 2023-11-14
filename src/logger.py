import logging
import os
from datetime import datetime

logs_path=os.path.join(os.getcwd(),"logs")
os.makedirs(logs_path,exist_ok=True)
LOG_FILE_NAME=f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"

LOG_FILE=os.path.join(logs_path, LOG_FILE_NAME)

logging.basicConfig(
    filename=LOG_FILE,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
