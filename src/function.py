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


def write_csv(name, name_1, value_1, name_2, value_2):
    # 初始化csv
    csv_path = init_csv(name.lower())

    # 读取csv
    with open(csv_path, 'r', newline='') as file:
        data = list(csv.reader(file))

    # 是否存在表头
    if not data:
        if value_2 == 0:
            data.append(["时间", name_1])
        else:
            data.append(["时间", name_1, name_2])

    # 创建数据
    today = datetime.now().strftime("%Y-%m-%d")
    if data[-1][0] != today:
        if value_2 == 0:
            data.append([today, value_1])
        else:
            data.append([today, value_1, value_2])

    # 若已有今日数据，则更新
    else:
        data[-1][1] = value_1
        if value_2 != 0:
            data[-1][2] = value_2

    # 写入csv
    with open(csv_path, 'w', newline='') as file:
        csv.writer(file).writerows(data)
