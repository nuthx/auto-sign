import os
import random
import configparser


def random_time(time):
    hour, minute = time.split(":")

    minute = "{:02d}".format(random.randint(int(minute), int(minute) + 8))
    second = "{:02d}".format(random.randint(1, 59))

    return f"{hour}:{str(minute)}:{str(second)}"


def init_config(filepath):
    config = configparser.ConfigParser()

    config.add_section("skland")
    config.set("skland", "token", "['']")

    config.add_section("psnine")
    config.set("psnine", "psnid", "")
    config.set("psnine", "shell", "")

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
        print(f"缺少{website}配置，跳过")
        print("———————————————————————————————————————")
        return 404
    else:
        cookies = f"{auth_name}={auth_value}; {salt_name}={salt_value}"
        return cookies
