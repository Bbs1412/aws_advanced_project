# This complete logger can be easily replaced by importing the logger module
# Implemented this only to try building a basic logger from scratch

import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
LOGGING_ENABLED = True if os.environ.get(
    "LOGGING", "false").lower() == 'true' else False


def get_timestamp():
    return datetime.now().strftime("%d-%m-%y %H:%M:%S")
    # return datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    # return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# print(get_timestamp())


def create_log(source: str, message: object, pre_lines=0, post_lines=0):
    if not LOGGING_ENABLED:
        return

    timestamp = get_timestamp()
    log = "\n" * pre_lines
    # log += f"[{timestamp}] '{source.upper().ljust(5)}' : {message}"
    source = f"'{source.upper()}'"

    log += f"[{timestamp}] {source.ljust(5)}: {message}"
    log += "\n" * post_lines

    with open('logs.txt', 'a') as f:
        f.write(log + '\n')


# create_log("app", "Server is live")
