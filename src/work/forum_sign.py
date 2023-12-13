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

    # 获取formhash
    log(f"{name_cn}(1/3) - 签到开始")
    response = requests.post(forum["sign_url"], headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    formhash = soup.select_one("#scbar_form input:nth-child(2)").get("value")

    # 执行签到
    sign_say = "%E7%AD%BE%E5%88%B0%E7%AD%BE%E5%88%B0%7E"
    sign_data = "formhash=" + formhash + "&qdxq=kx&qdmode=1&todaysay=" + sign_say + "&fastreply=0"
    response = requests.post(forum["sign_post"], data=sign_data, headers=headers)

    # 获取签到的返回信息
    soup_xml = BeautifulSoup(response.text, "xml")
    soup_html = BeautifulSoup(soup_xml.root.string, 'html.parser')
    sign_result = soup_html.select_one(".c").text.replace(".", "").strip()
    log(f"{name_cn}(2/3) - {sign_result}")

    # 获取论坛积分
    response = requests.get(forum["coin_url"], headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    coin_1 = soup.select_one(".creditl li").text.split(":")
    coin_2 = soup.select_one(".creditl li:nth-child(2)").text.split(":")
    name_1 = coin_1[0].strip()
    value_1 = int(coin_1[1].strip())
    name_2 = coin_2[0].strip()
    value_2 = int(coin_2[1].strip())

    # 写入csv
    write_csv(name, name_1, value_1, name_2, value_2)

    # 输出日志
    if value_2 == 0:
        log(f"{name_cn}(3/3) - {name_1}: {value_1}")
    else:
        log(f"{name_cn}(3/3) - {name_1}: {value_1}, {name_2}: {value_2}")
    log("———————————————————————————————————————")
