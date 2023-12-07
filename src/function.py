import os
import csv
import logging
import configparser
from datetime import datetime, timedelta


def log(content):
    now = datetime.now()
    time = now.strftime("%Y-%m-%d %H:%M:%S")

    logging.basicConfig(filename=f"{now.year}-{now.month}.log", level=logging.INFO, format="%(message)s")
    logging.info(f"[{time}] {content}")
    print(f"[{time}] {content}")


def next_time(added_second):
    current = datetime.now()
    delta = timedelta(seconds=added_second)
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


def init_csv(filename):
    # 创建文件夹
    if not os.path.exists("data"):
        os.mkdir("data")

    # 创建空文件
    filepath = os.path.join("data", filename + ".csv")
    if not os.path.exists(filepath):
        with open(filepath, 'w', newline='') as file:
            csv.writer(file)

    return filepath
