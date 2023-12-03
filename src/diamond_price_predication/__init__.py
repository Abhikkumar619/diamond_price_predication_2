import os
import sys
import logging 

log_dir="LOG"
log_file_path= os.path.join(log_dir, "running_log.log")
os.makedirs(log_dir, exist_ok=True)

logging_str="[%(asctime)s : %(levelname)s: %(module)s : %(message)s]"

logging.basicConfig(level=logging.INFO, format=logging_str, 
                    handlers=[
                        logging.FileHandler(log_file_path),
                        logging.StreamHandler(sys.stdout)
                    ])

logger=logging.getLogger("diamond_price_predication_project")

