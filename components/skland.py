import time
import json
import random
import requests
from components.function import *


def send_bark():
    config = configparser.ConfigParser()
    config.read("config.ini")
    bark = config.get("bark", "api")

    title = "森空岛（伪）"
    content = "理智恢复完成"
    icon = "https://img1.imgtp.com/2023/09/04/3ijFJfYG.png"

    requests.post(f"https://api.day.app/{bark}/{title}/{content}/?icon={icon}")


def skland_apcheck():
    config = configparser.ConfigParser()
    config.read("config.ini")
    uid = config.get("skland", "uid")
    cred = config.get("skland", "cred")

    url = f"https://zonai.skland.com/api/v1/game/player/info?uid={uid}"
    headers = {
        "User-Agent": "Skland/1.0.1 (com.hypergryph.skland; build:100001018; iOS 16.6.0) Alamofire/5.7.1",
        "cred": cred
    }

    # 获取理智信息
    response = requests.get(url, headers=headers).json()
    ap_data = response["data"]["status"]["ap"]

    time_now = time.time()
    time_complete = ap_data["completeRecoveryTime"]
    difference = time_complete - time_now
    return difference


def skland_apcheck_timer():
    check = 0

    while True:
        difference = skland_apcheck()

        if difference > 0:
            dif_hour = int(difference / 3600)
            dif_minute = int(difference % 3600 / 60)
            print(f"[{logtime(0)}] 明日方舟(1/1) - 理智恢复中，{dif_hour}小时{dif_minute}分后再次刷新")
            check = 0

            sleep_time = int(difference) + 3
            time.sleep(sleep_time)
        else:
            print(f"[{logtime(0)}] 明日方舟(1/2) - 理智已完全恢复，10分钟后再次刷新")
            if check == 0:
                print(f"[{logtime(0)}] 明日方舟(2/2) - 发送了Bark提醒")
                print(f"[{logtime(0)}] ———————————————————————————————————————————————")
                send_bark()
                check = 1
            else:
                print(f"[{logtime(0)}] 明日方舟(2/2) - 已提醒过，不再发送Bark提醒")
                print(f"[{logtime(0)}] ———————————————————————————————————————————————")
            time.sleep(600)


def skland_sign():
    config = configparser.ConfigParser()
    config.read("config.ini")
    uid = config.get("skland", "uid")
    cred = config.get("skland", "cred")

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
    print(f"[{logtime(0)}] {BLUE}明日方舟(1/3){RESET} - 每日签到开始")
    response = requests.post(url, data=json.dumps(data), headers=headers)

    # 获取签到返回内容
    result = json.loads(response.text)
    message = result["message"]

    if message == "OK":
        award_name = result["data"]["awards"][0]["resource"]["name"]
        award_count = result["data"]["awards"][0]["count"]
        print(f"[{logtime(0)}] {BLUE}明日方舟(2/3){RESET} - 获得了{award_name} x{award_count}")
    else:
        print(f"[{logtime(0)}] {BLUE}明日方舟(2/3){RESET} - {message}")


def skland_sign_timer():
    while True:
        # 间隔24小时以上
        random_time = random.randint(86400, 87000)

        # 开始签到
        skland_sign()
        print(f"[{logtime(0)}] {BLUE}明日方舟(3/3){RESET} - 下次将于{logtime(random_time)}开始签到")
        print(f"[{logtime(0)}] ———————————————————————————————————————————————")
        time.sleep(random_time)
