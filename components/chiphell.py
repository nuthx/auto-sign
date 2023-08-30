import time
import random
import requests
from bs4 import BeautifulSoup
from components.function import *


home_url = "https://www.tsdm39.com/forum.php"
credit_url = "https://www.chiphell.com/home.php?mod=spacecp&ac=credit&op=log&suboperation=creditrulelog"


def chiphell_sign():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "cookie": get_cookies("chiphell"),
        "connection": "Keep-Alive",
        "x-requested-with": "XMLHttpRequest",
        "referer": home_url,
        "content-type": "application/x-www-form-urlencoded"
    }

    print(f"[{logtime(0)}] {YELLOW}Chiphell签到{RESET} - 开始")

    # 先访问一次首页
    requests.get(home_url, headers=headers)
    time.sleep(random.randint(1, 3))

    # 执行签到并获取信息
    response = requests.get(credit_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    total_num = soup.select_one("div.bw0 table tr:nth-child(2) td:nth-child(2)").text
    cycle_num = soup.select_one("div.bw0 table tr:nth-child(2) td:nth-child(3)").text
    print(f"[{logtime(0)}] {YELLOW}Chiphell签到 - 累计签到{total_num}次，已循环{cycle_num}个周期{RESET}")


def chiphell_sign_timer():
    while True:
        # 间隔24小时以上
        random_time = random.randint(86400, 87000)

        # 开始签到
        chiphell_sign()
        print(f"[{logtime(0)}] {YELLOW}Chiphell签到{RESET} - 下次将于{logtime(random_time)}开始")
        time.sleep(random_time)
