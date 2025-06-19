import os
import logging
from logging.handlers import RotatingFileHandler

LOG_DIR='nabeeha_logs'
LOG_FILE='app.log'
LOG_PATH=os.path.join(LOG_DIR,LOG_FILE)

os.makedirs(LOG_DIR,exist_ok=True)

def create_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG) 
    handler = RotatingFileHandler(LOG_PATH, maxBytes=10*1024*1024, backupCount=5)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

logger = create_logger()
#now i shall be using this logger instead of print statements to log the outputs
