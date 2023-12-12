import os
import sys
import logging

logging_str="[%(asctime)s : %(levelname)s: %(module)s : %(message)s]"

log_dir="logs"
log_filepath=os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(level=logging.INFO,
                     format=logging_str, 
                     
                     handlers=[logging.FileHandler(log_filepath), # saving the log in directory.
                               logging.StreamHandler(sys.stdout) # print log in our terminal.
                               ]
                     )
logger=logging.getLogger("mlProjectLogger")