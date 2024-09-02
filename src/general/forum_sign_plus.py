import requests
from bs4 import BeautifulSoup

from src.coin import get_coin


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
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "cookie": COOKIE,
        "referer": URL + "/qiandao.php"
    }

    # 获取formhash
    print(f"{NAME}(1/3) - 签到开始")
    response = requests.post(URL + "/qiandao.php", headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    formhash = soup.select_one("#scbar_form input:nth-child(2)").get("value")

    # 执行签到
    sign_url_full = URL + "/qiandao.php?sign=" + formhash
    response = requests.post(sign_url_full, headers=headers)

    # 获取签到的返回信息
    if "已经打过卡" in response.text:
        print(f"{NAME}(2/3) - 今日已签，请勿重复进行")
    else:
        print(f"{NAME}(2/3) - 签到完成")

    # 获取论坛积分
    coin = get_coin(URL, headers)
    if coin:
        print(f"{NAME}(3/3) - {coin[0]}, {coin[1]}")
        print("——————————")
    else:
        print(f"{NAME}(3/3) - 余额获取失败")
        print("——————————")
