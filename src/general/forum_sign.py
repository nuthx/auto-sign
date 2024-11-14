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

    try:
        # 获取formhash
        print(f"{NAME}(1/3) - 签到开始")
        response = requests.post(URL + "/plugin.php?id=dsu_paulsign:sign", headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        formhash = soup.select_one("#scbar_form input:nth-child(2)").get("value")

        # 执行签到
        sign_say = "%E7%AD%BE%E5%88%B0%E7%AD%BE%E5%88%B0%7E"
        sign_data = "formhash=" + formhash + "&qdxq=kx&qdmode=1&todaysay=" + sign_say + "&fastreply=0"
        response = requests.post(URL + "/plugin.php?id=dsu_paulsign:sign&operation=qiandao&infloat=1&inajax=1", data=sign_data, headers=headers)

        # 获取签到的返回信息
        soup_xml = BeautifulSoup(response.text, "xml")
        soup_html = BeautifulSoup(soup_xml.root.string, 'html.parser')
        sign_result = soup_html.select_one(".c").text.replace(".", "").strip()
        print(f"{NAME}(2/3) - {sign_result}")

        # 获取论坛积分
        coin = get_coin(URL, headers)
        if coin:
            print(f"{NAME}(3/3) - {coin[0]}, {coin[1]}")
            print("——————————")
        else:
            print(f"{NAME}(3/3) - 余额获取失败")
            print("——————————")

    except Exception as e:
        print(f"{NAME}(3/3) - 签到失败，原因：{e}")
        print("——————————")
