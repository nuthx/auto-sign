import time
import random
import requests
import configparser
from bs4 import BeautifulSoup
from components.function import *


home_url = "https://www.tsdm39.com/forum.php"
credit_url = "https://www.chiphell.com/home.php?mod=spacecp&ac=credit&op=log&suboperation=creditrulelog"


def get_chiphell_cookies():
    config = configparser.ConfigParser()
    config.read("config.ini")

    auth_name = config.get("chiphell", "auth_name")
    auth_value = config.get("chiphell", "auth_value")
    salt_name = config.get("chiphell", "salt_name")
    salt_value = config.get("chiphell", "salt_value")

    chiphell_cookies = f"{auth_name}={auth_value}; {salt_name}={salt_value}"
    return chiphell_cookies


def chiphell_sign():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "cookie": get_chiphell_cookies(),
        "connection": "Keep-Alive",
        "x-requested-with": "XMLHttpRequest",
        "referer": home_url,
        "content-type": "application/x-www-form-urlencoded"
    }

    print("-------------------------")
    print(f"[{logtime(0)}] {YELLOW}开始签到 - Chiphell{RESET}")

    # 先访问一次首页
    requests.get(home_url, headers=headers)
    time.sleep(random.randint(1, 3))

    # 执行签到并获取信息
    response = requests.get(credit_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    total_num = soup.select_one("div.bw0 table tr:nth-child(2) td:nth-child(2)").text
    cycle_num = soup.select_one("div.bw0 table tr:nth-child(2) td:nth-child(3)").text
    print(f"[{logtime(0)}] 签到成功 - 累计签到{total_num}次，已循环{cycle_num}个周期")


def chiphell_sign_timer():
    while True:
        # 等待60秒
        # time.sleep(60)

        # 间隔23-24小时
        random_time = random.randint(82800, 86400)

        # 开始签到
        chiphell_sign()
        print(f"[{logtime(0)}] 全部完成 - 下次签到将于{logtime(random_time)}开始")
        time.sleep(random_time)
