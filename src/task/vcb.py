import time
import random
import requests
from bs4 import BeautifulSoup
from components.function import *


home_url = "https://bbs.acgrip.com/"
credit_url = "https://bbs.acgrip.com/home.php?mod=spacecp&ac=credit&op=base"


def vcb_sign():
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "cookie": get_cookies("vcb"),
        "referer": home_url
    }

    # 访问首页签到
    log("VCB(1/4) - 签到开始")
    requests.get(home_url, headers=headers)
    time.sleep(random.randint(1, 2))
    log("VCB(2/4) - 完成签到尝试，结果未知")

    # 获取VC币
    response = requests.get(credit_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    activity = soup.select_one(".creditl li").text.replace("活跃度:", "").strip()
    coin = soup.select_one(".creditl li:nth-child(2)").text.replace("VC币:", "").strip()
    log(f"VCB(3/4) - 当前拥有{activity}活跃度，{coin}VC币")


def vcb_sign_timer():
    while True:
        # 间隔24小时以上
        random_time = random.randint(86400, 87000)

        # 开始签到
        vcb_sign()
        log(f"VCB(4/4) - 下次将于{next_time(random_time)}开始签到")
        log("———————————————————————————————————————————————")
        time.sleep(random_time)
