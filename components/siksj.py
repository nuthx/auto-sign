import time
import random
import requests
from bs4 import BeautifulSoup
from components.function import *
import xml.etree.ElementTree as ET


sign_url = "https://www.4ksj.com/qiandao/"
sign_post = "https://www.4ksj.com/qiandao/?mod=sign&operation=qiandao&format=empty&inajax=1&ajaxtarget="
coin_url = "https://www.4ksj.com/home.php?mod=spacecp&ac=credit"


def siksj_sign():
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "cookie": get_cookies("siksj"),
        "referer": sign_url
    }

    # 获取formhash
    log("4K世界(1/4) - 签到开始")
    response = requests.post(sign_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    formhash = soup.select_one("#scbar_form input:nth-child(2)").get("value")

    # 执行签到
    sign_url_full = sign_post + "&formhash=" + formhash
    response = requests.post(sign_url_full, headers=headers)

    # 获取签到的返回信息
    result = ET.fromstring(response.text).text
    if result is None:
        log("4K世界(2/4) - 签到完成")
    else:
        log(f"4K世界(2/4) - {result}，请勿重复进行")

    # 获取当前积分数
    response = requests.post(coin_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    credit = soup.select_one(".creditl li").text
    credit = credit.replace("K币:", "").replace("个", "").replace("立即充值»", "").strip()
    log(f"4K世界(3/4) - 当前拥有{credit}个K币")


def siksj_sign_timer():
    while True:
        # 间隔24小时以上
        random_time = random.randint(86400, 87000)

        # 开始签到
        siksj_sign()
        log(f"4K世界(4/4) - 下次将于{next_time(random_time)}开始签到")
        log("———————————————————————————————————————————————")
        time.sleep(random_time)
