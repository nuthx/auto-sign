import time
import requests
from bs4 import BeautifulSoup
from src.function import *


def do(forum):
    name = forum["name"]

    cookies = get_cookies(name.lower())

    if cookies == 404:
        return

    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "cookie": cookies,
        "referer": forum["home_url"]
    }

    # 访问首页
    print(f"{name}(1/3) - 浏览论坛首页")
    requests.get(forum["home_url"], headers=headers)
    time.sleep(random.randint(1, 2))
    print(f"{name}(2/3) - 完成每日访问")

    # 获取论坛积分
    response = requests.get(forum["coin_url"], headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    coin_1 = soup.select_one(".creditl li").text.split(":")
    coin_2 = soup.select_one(".creditl li:nth-child(2)").text.split(":")
    name_1 = coin_1[0].strip()
    value_1 = int(coin_1[1].strip())
    name_2 = coin_2[0].strip()
    value_2 = int(coin_2[1].strip())

    # 输出日志
    if value_2 == 0:
        print(f"{name}(3/3) - {name_1}: {value_1}")
    else:
        print(f"{name}(3/3) - {name_1}: {value_1}, {name_2}: {value_2}")
    print("———————————————————————————————————————")
