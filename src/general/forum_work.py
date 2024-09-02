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

    # 必须要这个content-type, 否则没法接收
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "cookie": COOKIE,
        "referer": URL + "/plugin.php?id=dsu_paulsign:sign"
    }

    # 打工之前必须访问过一次网页
    print(f"{NAME}(1/3) - 打工开始")
    requests.get(URL + "/plugin.php?id=np_cliworkdz:work", headers=headers)

    # 8次打工
    for i in range(8):
        response = requests.post(URL + "/plugin.php?id=np_cliworkdz:work", data="act=clickad", headers=headers)
        print(f"{NAME}(2/3) - 打工第{i+1}次")
        if "必须与上一次间隔" in response.text:
            break
        if i == 7:
            print(f"{NAME}(2/3) - 完成8次打工")

    # 获取打工的返回信息
    response = requests.post(URL + "/plugin.php?id=np_cliworkdz:work", data="act=getcre", headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    sign_result = soup.select_one("#messagetext").text
    sign_result = sign_result.replace("如果你的浏览器没有自动跳转，请点击此链接", "").strip()
    print(f"{NAME}(2/3) - {sign_result}")

    # 获取论坛积分
    coin = get_coin(URL, headers)
    if coin:
        print(f"{NAME}(3/3) - {coin[0]}, {coin[1]}")
        print("——————————")
    else:
        print(f"{NAME}(3/3) - 余额获取失败")
        print("——————————")
