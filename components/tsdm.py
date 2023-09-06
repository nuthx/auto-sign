import time
import random
import requests
from bs4 import BeautifulSoup
from components.function import *


home_url = "https://www.tsdm39.com/forum.php"
sign_url = "https://www.tsdm39.com/plugin.php?id=dsu_paulsign:sign"
sign_post = "https://www.tsdm39.com/plugin.php?id=dsu_paulsign:sign&operation=qiandao&infloat=1&inajax=1"
work_url = "https://www.tsdm39.com/plugin.php?id=np_cliworkdz:work"
coin_url = "https://www.tsdm39.com/home.php?mod=spacecp&ac=credit&showcredit=1"


def tsdm_sign():
    # 必须要这个content-type, 否则没法接收
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "cookie": get_cookies("tsdm"),
        "referer": sign_url
    }

    # 获取formhash
    print(f"[{logtime(0)}] {MAGENTA}天使动漫(1/4){RESET} - 签到开始")
    response = requests.post(sign_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    formhash = soup.select_one("#scbar_form input:nth-child(2)").get("value")

    # 执行签到
    sign_data = "formhash=" + formhash + "&qdxq=wl&qdmode=3&todaysay=&fastreply=1"
    response = requests.post(sign_post, data=sign_data, headers=headers)

    # 获取签到的返回信息
    soup_xml = BeautifulSoup(response.text, "xml")
    soup_html = BeautifulSoup(soup_xml.root.string, 'html.parser')
    sign_result = soup_html.select_one(".c").text.replace(".", "").strip()
    print(f"[{logtime(0)}] {MAGENTA}天使动漫(2/4){RESET} - " + sign_result)

    # 获取当前积分数
    response = requests.post(coin_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    credit = soup.select_one(".creditl li").text.replace("天使币:", "").strip()
    print(f"[{logtime(0)}] {MAGENTA}天使动漫(3/4){RESET} - 当前拥有{credit}天使币")


def tsdm_sign_timer():
    while True:
        # 间隔24小时以上
        random_time = random.randint(86400, 87000)

        # 开始签到
        tsdm_sign()
        print(f"[{logtime(0)}] {MAGENTA}天使动漫(4/4){RESET} - 下次将于{logtime(random_time)}开始签到")
        print(f"[{logtime(0)}] ———————————————————————————————————————————————")
        time.sleep(random_time)


def tsdm_work():
    # 必须要这个content-type, 否则没法接收
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "cookie": get_cookies("tsdm"),
        "referer": home_url
    }

    # 打工之前必须访问过一次网页
    print(f"[{logtime(0)}] {CYAN}天使动漫(1/4){RESET} - 打工开始")
    requests.get(work_url, headers=headers)

    # 检查是否已经打过工
    response = requests.post(work_url, data="act=clickad", headers=headers)
    if "必须与上一次间隔" in response.text:
        print(f"[{logtime(0)}] {CYAN}天使动漫(2/4){RESET} - 该账户已经打工过")
        print(f"[{logtime(0)}] {CYAN}天使动漫(3/4){RESET} - 停止打工")
        return

    # 尝试8次打工
    for i in range(8):
        requests.post(work_url, data="act=clickad", headers=headers)
        print(f"[{logtime(0)}] {CYAN}天使动漫(2/4){RESET} - 打工第" + str(i+1) + "次")

    # 获取打工的返回信息
    response = requests.post(work_url, data="act=getcre", headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    sign_result = soup.select_one("#messagetext").text
    sign_result = sign_result.replace("如果你的浏览器没有自动跳转，请点击此链接", "").strip()
    print(f"[{logtime(0)}] {CYAN}天使动漫(2/4){RESET} - " + sign_result)

    # 获取当前积分数
    response = requests.post(coin_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    credit = soup.select_one(".creditl li").text.replace("天使币:", "").strip()
    print(f"[{logtime(0)}] {CYAN}天使动漫(3/4){RESET} - 当前拥有{credit}天使币")


def tsdm_work_timer():
    while True:
        # 间隔6小时多点
        random_time = random.randint(21600, 21700)

        # 开始打工
        tsdm_work()
        print(f"[{logtime(0)}] {CYAN}天使动漫(4/4){RESET} - 下次将于{logtime(random_time)}再次打工")
        print(f"[{logtime(0)}] ———————————————————————————————————————————————")
        time.sleep(random_time)
