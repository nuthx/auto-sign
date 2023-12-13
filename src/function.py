import os
import csv
import random
import logging
import configparser
from datetime import datetime


def random_time(time):
    hour, minute = time.split(":")

    minute = "{:02d}".format(random.randint(int(minute), int(minute) + 8))
    second = "{:02d}".format(random.randint(1, 59))

    return f"{hour}:{str(minute)}:{str(second)}"


def log(content):
    # 创建文件夹
    check_folder("log")

    now = datetime.now()
    time = now.strftime("%Y-%m-%d %H:%M:%S")

    filepath = os.path.join("log", f"{now.year}-{now.month}.log")

    logging.basicConfig(filename=filepath, level=logging.INFO, format="%(message)s")
    logging.info(f"[{time}] {content}")
    print(f"[{time}] {content}")


def check_folder(folder_name):
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)


def init_config(filepath):
    config = configparser.ConfigParser()

    config.add_section("skland")
    config.set("skland", "token", "['']")

    config.add_section("tsdm")
    config.set("tsdm", "auth_name", "")
    config.set("tsdm", "auth_value", "")
    config.set("tsdm", "salt_name", "")
    config.set("tsdm", "salt_value", "")

    config.add_section("chiphell")
    config.set("chiphell", "auth_name", "")
    config.set("chiphell", "auth_value", "")
    config.set("chiphell", "salt_name", "")
    config.set("chiphell", "salt_value", "")

    config.add_section("skyey")
    config.set("skyey", "auth_name", "")
    config.set("skyey", "auth_value", "")
    config.set("skyey", "salt_name", "")
    config.set("skyey", "salt_value", "")

    config.add_section("sayhuahuo")
    config.set("sayhuahuo", "auth_name", "")
    config.set("sayhuahuo", "auth_value", "")
    config.set("sayhuahuo", "salt_name", "")
    config.set("sayhuahuo", "salt_value", "")

    config.add_section("sksj")
    config.set("sksj", "auth_name", "")
    config.set("sksj", "auth_value", "")
    config.set("sksj", "salt_name", "")
    config.set("sksj", "salt_value", "")

    config.add_section("vcb")
    config.set("vcb", "auth_name", "")
    config.set("vcb", "auth_value", "")
    config.set("vcb", "salt_name", "")
    config.set("vcb", "salt_value", "")

    # 写入配置内容
    with open(filepath, "w", encoding="utf-8") as content:
        config.write(content)


def get_cookies(website):
    # 创建文件夹
    check_folder("config")

    # 创建空文件
    filepath = os.path.join("config", "config.ini")
    if not os.path.exists(filepath):
        init_config(filepath)

    # 读取当前配置
    config = configparser.ConfigParser()
    config.read(filepath)

    # 获取配置内容
    auth_name = config.get(website, "auth_name")
    auth_value = config.get(website, "auth_value")
    salt_name = config.get(website, "salt_name")
    salt_value = config.get(website, "salt_value")

    if "" in (auth_name, auth_value, salt_name, salt_value):
        log(f"缺少{website}配置，跳过")
        log("———————————————————————————————————————")
        return 404
    else:
        cookies = f"{auth_name}={auth_value}; {salt_name}={salt_value}"
        return cookies


def init_csv(filename):
    # 创建文件夹
    check_folder("data")

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
