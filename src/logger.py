import os
import logging
from datetime import datetime

# Create log file name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Create logs folder path
logs_dir = os.path.join(os.getcwd(), "logs")

# Create logs folder if it does not exist
os.makedirs(logs_dir, exist_ok=True)

# Final log file path (JOIN ONLY ONCE)
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s'
)

