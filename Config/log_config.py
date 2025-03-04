
import datetime
import multiprocessing
import os

#create log directory if it doesnot exist

log_directory="logs"
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

# getting process id to create a unique file for each parallel test process

process_id=multiprocessing.current_process().pid

log_file = os.path.join(log_directory, f"test_log_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S_%f')}_pid{process_id}.log")



