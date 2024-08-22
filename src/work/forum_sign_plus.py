import re
import requests
from bs4 import BeautifulSoup
from src.function import *


def do(forum):
    name = forum["name"]
    name_cn = forum["name_cn"]

    cookies = get_cookies(name.lower())

    if cookies == 404:
        return

    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "cookie": cookies,
        "referer": forum["sign_url"]
    }

    # 获取formhash
    print(f"{name_cn}(1/3) - 签到开始")
    response = requests.post(forum["sign_url"], headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    formhash = soup.select_one("#scbar_form input:nth-child(2)").get("value")

    # 执行签到
    sign_url_full = forum["sign_post"] + formhash
    response = requests.post(sign_url_full, headers=headers)

    # 获取签到的返回信息
    if "已经打过卡" in response.text:
        print(f"{name_cn}(2/3) - 今日已签，请勿重复进行")
    else:
        print(f"{name_cn}(2/3) - 签到完成")

    # 获取论坛积分
    response = requests.get(forum["coin_url"], headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    coin_1 = soup.select_one(".creditl li").text.split(":")
    name_1 = coin_1[0].strip()
    value_1 = int(re.sub(r'\D', '', coin_1[1]))

    # 输出日志
    print(f"{name_cn}(3/3) - {name_1}: {value_1}")
    print("———————————————————————————————————————")
