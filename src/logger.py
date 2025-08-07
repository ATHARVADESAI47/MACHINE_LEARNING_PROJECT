import os
import logging
from datetime import datetime

# Step 1: Create a unique log filename with a timestamp
log_file = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Step 2: Define the logs directory path
log_path = os.path.join(os.getcwd(), 'logs')
os.makedirs(log_path, exist_ok=True)  # Create logs folder if it doesn't exist

# Step 3: Full path to the log file
log_file_path = os.path.join(log_path, log_file)

# Step 4: Configure logging
logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s'
)
