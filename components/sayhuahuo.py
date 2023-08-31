import time
import random
import requests
from bs4 import BeautifulSoup
from components.function import *


home_url = "https://www.sayhuahuo.net/"
coin_url = "https://www.sayhuahuo.net/home.php?mod=spacecp&ac=credit&showcredit=1"
sign_url = "https://www.sayhuahuo.net/dsu_paulsign-sign.html"
sign_post = "https://www.sayhuahuo.net/plugin.php?id=dsu_paulsign:sign&operation=qiandao&infloat=1&inajax=1"


def sayhuahuo_sign():
    # 必须要这个content-type, 否则没法接收
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "cookie": get_cookies("sayhuahuo"),
        "referer": sign_url
    }

    # 获取formhash
    print(f"[{logtime(0)}] {MAGENTA}花火学园(1/4){RESET} - 签到开始")
    response = requests.post(sign_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    formhash = soup.select_one("#scbar_form input:nth-child(2)").get("value")

    # 执行签到
    sign_say = "%E7%AD%BE%E5%88%B0%E7%AD%BE%E5%88%B0%7E"
    sign_data = "formhash=" + formhash + "&qdxq=kx&qdmode=1&todaysay=" + sign_say + "&fastreply=0"
    response = requests.post(sign_post, data=sign_data, headers=headers)

    # 获取签到的返回信息
    soup_xml = BeautifulSoup(response.text, "xml")
    soup_html = BeautifulSoup(soup_xml.root.string, 'html.parser')
    sign_result = soup_html.select_one(".c").text.strip()
    print(f"[{logtime(0)}] {MAGENTA}花火学园(2/4){RESET} - " + sign_result)

    # 获取当前积分数
    response = requests.post(coin_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    exp = soup.select_one(".creditl li:nth-child(2)").text.replace("经验:", "").strip()
    credit = soup.select_one(".creditl li").text.replace("学分:", "").strip()
    print(f"[{logtime(0)}] {MAGENTA}花火学园(3/4){RESET} - 当前拥有{credit}学分，{exp}经验")


def sayhuahuo_sign_timer():
    while True:
        # 间隔24小时以上
        random_time = random.randint(86400, 87000)

        # 开始签到
        sayhuahuo_sign()
        print(f"[{logtime(0)}] {MAGENTA}花火学园(4/4){RESET} - 下次将于{logtime(random_time)}开始")
        time.sleep(random_time)
