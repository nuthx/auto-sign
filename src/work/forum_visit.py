import time
import random
import requests
from bs4 import BeautifulSoup
from src.function import *


def do(forum):
    name = forum["name"]

    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "cookie": get_cookies(name.lower()),
        "referer": forum["home_url"]
    }

    # 访问首页
    log(f"{name}(1/3) - 浏览论坛首页")
    requests.get(forum["home_url"], headers=headers)
    time.sleep(random.randint(1, 2))
    log(f"{name}(2/3) - 完成每日访问")

    # 获取论坛积分
    response = requests.get(forum["credit_url"], headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    coin_1 = soup.select_one(".creditl li").text.split(":")
    coin_name_1 = coin_1[0].strip()
    coin_value_1 = coin_1[1].strip()
    coin_name_2 = 0
    coin_value_2 = 0

    # 如果论坛有两种积分类型，获取第二种积分
    if forum["coin_type"] == 2:
        coin_2 = soup.select_one(".creditl li:nth-child(2)").text.split(":")
        coin_name_2 = coin_2[0].strip()
        coin_value_2 = coin_2[1].strip()

    # 初始化csv
    csv_path = init_csv(name.lower())

    # 读取csv
    with open(csv_path, 'r', newline='') as file:
        data = list(csv.reader(file))

    # 是否存在表头
    if not data:
        if coin_value_2 == 0:
            data.append(["时间", coin_name_1])
        else:
            data.append(["时间", coin_name_1, coin_name_2])

    # 创建数据
    today = datetime.now().strftime("%Y-%m-%d")
    if data[-1][0] != today:
        if coin_value_2 == 0:
            data.append([today, coin_value_1])
        else:
            data.append([today, coin_value_1, coin_value_2])

    # 若已有今日数据，则更新
    else:
        data[-1][1] = coin_value_1
        if coin_value_2 != 0:
            data[-1][2] = coin_value_2

    # 写入csv
    with open(csv_path, 'w', newline='') as file:
        csv.writer(file).writerows(data)

    # 输出日志
    if coin_value_2 == 0:
        log(f"{name}(3/3) - {coin_name_1}: {coin_value_1}")
    else:
        log(f"{name}(3/3) - {coin_name_1}: {coin_value_1}, {coin_name_2}: {coin_value_2}")
    log("———————————————————————————————————————")
