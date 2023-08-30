import configparser
from datetime import datetime, timedelta


RESET = "\033[0m"
BLACK = "\033[0;30m"
RED = "\033[0;31m"
GREEN = "\033[0;32m"
YELLOW = "\033[0;33m"
BLUE = "\033[0;34m"
MAGENTA = "\033[0;35m"
CYAN = "\033[0;36m"
WHITE = "\033[0;37m"


def logtime(add_second):
    if add_second == 0:
        time = datetime.now()
        # time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    else:
        current = datetime.now()
        delta = timedelta(seconds=add_second)
        time = current + delta
        time = time.strftime("%Y-%m-%d %H:%M:%S")
    return time


def get_cookies(website):
    config = configparser.ConfigParser()
    config.read("config.ini")

    auth_name = config.get(website, "auth_name")
    auth_value = config.get(website, "auth_value")
    salt_name = config.get(website, "salt_name")
    salt_value = config.get(website, "salt_value")

    cookies = f"{auth_name}={auth_value}; {salt_name}={salt_value}"
    return cookies
