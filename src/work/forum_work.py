import requests
from bs4 import BeautifulSoup
from src.function import *


def do(forum):
    name = forum["name"]
    name_cn = forum["name_cn"]

    cookies = get_cookies(name.lower())

    if cookies == 404:
        return

    # 必须要这个content-type, 否则没法接收
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "cookie": cookies,
        "referer": forum["sign_url"]
    }

    # 打工之前必须访问过一次网页
    print(f"{name_cn}(1/3) - 打工开始")
    requests.get(forum["work_url"], headers=headers)

    # 8次打工
    for i in range(8):
        response = requests.post(forum["work_url"], data="act=clickad", headers=headers)
        print(f"{name_cn}(2/3) - 打工第{i+1}次")
        if "必须与上一次间隔" in response.text:
            break
        if i == 7:
            print(f"{name_cn}(2/3) - 完成8次打工")

    # 获取打工的返回信息
    response = requests.post(forum["work_url"], data="act=getcre", headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    sign_result = soup.select_one("#messagetext").text
    sign_result = sign_result.replace("如果你的浏览器没有自动跳转，请点击此链接", "").strip()
    print(f"{name_cn}(2/3) - {sign_result}")

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
        print(f"{name_cn}(3/3) - {name_1}: {value_1}")
    else:
        print(f"{name_cn}(3/3) - {name_1}: {value_1}, {name_2}: {value_2}")
    print("———————————————————————————————————————")
