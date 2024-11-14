import time
import random
import requests

from src.coin import get_coin_wp


def do(forum):
    NAME = forum["name"]
    COOKIE = forum["cookie"]
    URL = forum["url"]

    if not COOKIE:
        print(f"{NAME}(1/1) - 缺少配置文件，跳过")
        print("——————————")
        return

    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "cookie": COOKIE,
        "referer": URL
    }

    try:
        # 访问首页
        print(f"{NAME}(1/3) - 浏览论坛首页")
        requests.get(URL, headers=headers)
        time.sleep(random.randint(1, 2))
        print(f"{NAME}(2/3) - 完成每日访问")

        # 获取论坛积分
        coin = get_coin_wp(URL, headers)
        if coin:
            print(f"{NAME}(3/3) - {coin}")
            print("——————————")
        else:
            print(f"{NAME}(3/3) - 余额获取失败")
            print("——————————")

    except Exception as e:
        print(f"PSNINE(3/3) - 浏览失败，原因：{e}")
        print("——————————")
