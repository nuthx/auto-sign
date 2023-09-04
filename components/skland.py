import time
import requests
import configparser


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
    difference = skland_apcheck()

    if difference > 0:
        dif_hour = int(difference / 3600)
        dif_minute = int(difference % 3600 / 60)
        print(f"明日方舟 - 理智恢复中，{dif_hour}小时{dif_minute}分后再次刷新")

        sleep_time = int(difference) + 3
        time.sleep(sleep_time)
    else:
        print(f"明日方舟 - 理智已完全恢复，10分钟后再次刷新")
        send_bark()
        time.sleep(600)
