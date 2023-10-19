import time
import json
import random
import requests
from components.function import *


def skland_sign(num):
    config = configparser.ConfigParser()
    config.read("config.ini")
    uid = config.get(f"skland_{num}", "uid")
    cred = config.get(f"skland_{num}", "cred")

    url = "https://zonai.skland.com/api/v1/game/attendance"

    headers = {
        "content-type": "application/json",
        "User-Agent": "Skland/1.0.1 (com.hypergryph.skland; build:100001018; iOS 16.6.0) Alamofire/5.7.1",
        "cred": cred,
        "os": "iOS",
        "platform": "2",
        "manufacturer": "Apple",
    }

    data = {
        "uid": uid,
        "gameId": 1
    }

    # 签到
    log(f"明日方舟_{num}(1/3) - 签到开始")
    response = requests.post(url, data=json.dumps(data), headers=headers)

    # 获取签到返回内容
    result = json.loads(response.text)
    message = result["message"]

    if message == "OK":
        award_name = result["data"]["awards"][0]["resource"]["name"]
        award_count = result["data"]["awards"][0]["count"]
        log(f"明日方舟_{num}(2/3) - 获得了{award_name} x{award_count}")
    else:
        log(f"明日方舟_{num}(2/3) - {message}")


def skland_sign_timer(num):
    while True:
        # 间隔24小时以上
        random_time = random.randint(86400, 87000)

        # 开始签到
        skland_sign(num)
        log(f"明日方舟_{num}(3/3) - 下次将于{next_time(random_time)}开始签到")
        log("———————————————————————————————————————————————")
        time.sleep(random_time)
