import time
import random
import requests
from bs4 import BeautifulSoup
from components.function import *


home_url = "https://www.chiphell.com/forum.php"
credit_url = "https://www.chiphell.com/home.php?mod=spacecp&ac=credit&op=base"


def chiphell_sign():
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "cookie": get_cookies("chiphell"),
        "referer": home_url
    }

    # 访问首页签到
    print(f"[{logtime(0)}] {YELLOW}Chiphell(1/4){RESET} - 签到开始")
    requests.get(home_url, headers=headers)
    time.sleep(random.randint(1, 2))
    print(f"[{logtime(0)}] {YELLOW}Chiphell(2/4){RESET} - 完成签到尝试，结果未知")

    # 获取邪恶指数
    response = requests.get(credit_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    evil = soup.select_one(".creditl li").text.replace("邪恶指数:", "").strip()
    print(f"[{logtime(0)}] {YELLOW}Chiphell(3/4){RESET} - 当前拥有{evil}邪恶指数")


def chiphell_sign_timer():
    while True:
        # 间隔24小时以上
        random_time = random.randint(86400, 87000)

        # 开始签到
        chiphell_sign()
        print(f"[{logtime(0)}] {YELLOW}Chiphell(4/4){RESET} - 下次将于{logtime(random_time)}开始签到")
        time.sleep(random_time)
