
import datetime
import multiprocessing
import os
import logging
from typing import Optional

# #create log directory if it doesnot exist

# log_directory="logs"
# if not os.path.exists(log_directory):
#     os.makedirs(log_directory)

# # getting process id to create a unique file for each parallel test process

# process_id=multiprocessing.current_process().pid

# log_file = os.path.join(log_directory, f"test_log_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S_%f')}_pid{process_id}.log")


def logging_setup(log_directory: str= "logs", log_level : int =logging.INFO)-> logging.Logger:

    """
    Sets up logging with a file handler and console handler.

    Args:
        log_directory: Directory where log files will be stored.
        log_level: Logging level (e.g., logging.INFO, logging.DEBUG).

    Returns:
        logging.Logger: Configured logger instance.
    """

    #create log directory if doesnot exist
    if not os.path.exists(log_directory):
        os.makedirs(log_directory, exist_ok=True)

    # get the process id for the unique log file names in parallel execution
    process_id = multiprocessing.current_process().pid

    # Generate a unique log file name
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S_%f")
    log_file = os.path.join(log_directory, f"test_log_{timestamp}_pid{process_id}.log")

    # Create and configure logger
    logger = logging.getLogger(f"test_logger_{process_id}")
    logger.setLevel(log_level)

    # Avoid duplicate handlers if logger is already configured
    if logger.hasHandlers():
        logger.handlers.clear()

    # Define log format
    log_format = "%(asctime)s [%(levelname)s] [%(process)d] %(message)s"
    formatter = logging.Formatter(log_format)

    # File handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(log_level)
    file_handler.setFormatter(formatter)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)
    console_handler.setFormatter(formatter)

    # Add handlers to logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
