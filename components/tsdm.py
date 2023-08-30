import time
import random
import requests
import configparser
from components.function import *


home_url = "https://www.tsdm39.com/forum.php"
sign_url = "https://www.tsdm39.com/plugin.php?id=dsu_paulsign:sign"
sign_param = sign_url + "&operation=qiandao&infloat=1&sign_as=1&inajax=1"
work_url = "https://www.tsdm39.com/plugin.php?id=np_cliworkdz:work"


def get_tsdm_cookies():
    config = configparser.ConfigParser()
    config.read("config.ini")

    auth_name = config.get("tsdm", "auth_name")
    auth_value = config.get("tsdm", "auth_value")
    salt_name = config.get("tsdm", "salt_name")
    salt_value = config.get("tsdm", "salt_value")

    tsdm_cookies = f"{auth_name}={auth_value}; {salt_name}={salt_value}"
    return tsdm_cookies


def tsdm_sign():
    # 必须要这个content-type, 否则没法接收
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "cookie": get_tsdm_cookies(),
        "connection": "Keep-Alive",
        "x-requested-with": "XMLHttpRequest",
        "referer": home_url,
        "content-type": "application/x-www-form-urlencoded"
    }

    print(f"[{logtime(0)}] {MAGENTA}TSDM签到{RESET} - 开始")
    s = requests.session()
    response = s.get(sign_url, headers=headers).text

    form_start = response.find("formhash=") + 9  # 此处9个字符
    formhash = response[form_start:form_start + 8]  # formhash 8位

    # formhash, 签到心情, 签到模式(不发言)
    sign_data = "formhash=" + formhash + "&qdxq=wl&qdmode=3&todaysay=&fastreply=1"

    # 开始签到
    response = requests.post(sign_param, data=sign_data, headers=headers)

    # 返回结果
    if "恭喜你签到成功" in response.text:
        print(f"[{logtime(0)}] {MAGENTA}TSDM签到 - 成功{RESET}")
    elif "今日已经签到" in response.text:
        print(f"[{logtime(0)}] {MAGENTA}TSDM签到 - 今日已签到过{RESET}")
    elif "已经过了签到时间段" in response.text or "签到时间还没有到" in response.text:
        print(f"[{logtime(0)}] {MAGENTA}TSDM签到 - 目前不在签到时间段{RESET}")
    else:
        print(f"[{logtime(0)}] {MAGENTA}TSDM签到 - 未知原因失败{RESET}")


def tsdm_sign_timer():
    while True:
        # 间隔24小时以上
        random_time = random.randint(86400, 87000)

        # 开始签到
        tsdm_sign()
        print(f"[{logtime(0)}] {MAGENTA}TSDM签到{RESET} - 下次将于{logtime(random_time)}开始")
        time.sleep(random_time)


def tsdm_work():
    # 必须要这个content-type, 否则没法接收
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "cookie": get_tsdm_cookies(),
        "connection": "Keep-Alive",
        "x-requested-with": "XMLHttpRequest",
        "referer": home_url,
        "content-type": "application/x-www-form-urlencoded"
    }

    # 打工之前必须访问过一次网页
    print(f"[{logtime(0)}] {CYAN}TSDM打工{RESET} - 开始")
    requests.get(work_url, headers=headers)

    # 检查是否已经打过工
    response = requests.post(work_url, data="act=clickad", headers=headers)
    if "必须与上一次间隔" in response.text:
        print(f"[{logtime(0)}] {CYAN}TSDM打工 - 该账户已经打工过{RESET}")
        return

    # 总共6次打工, 实际打工8次保险
    for i in range(7):
        response = requests.post(work_url, data="act=clickad", headers=headers)  # 进行打工

        wait_time = round(random.uniform(0.5, 1), 2)  # 等待0.50-1.00秒
        time.sleep(wait_time)
        # print(f"点击广告: 第{i+1}次, 等待{wait_time}秒, 服务器标识:{response.text}")

        if int(response.text) > 1629134400:
            print(f"[{logtime(0)}] {CYAN}TSDM打工 - 检测到作弊判定, 请尝试重新运行{RESET}")
            break
        elif int(response.text) >= 6:  # 已点击6次, 停止
            break
        else:
            continue

    # 打工完成，点击领取天使币
    response = requests.post(work_url, data="act=getcre", headers=headers)

    # 返回结果
    if "成功领取了奖励天使币" in response.text:
        print(f"[{logtime(0)}] {CYAN}TSDM打工 - 成功{RESET}")
    elif "作弊" in response.text:
        print(f"[{logtime(0)}] {CYAN}TSDM打工 - 发现作弊判定{RESET}")
    elif "请先登录再进行点击任务" in response.text:
        print(f"[{logtime(0)}] {CYAN}TSDM打工 - cookie失效{RESET}")
    elif "服务器负荷较重" in response.text:
        print(f"[{logtime(0)}] {CYAN}TSDM打工 - 服务器负荷较重{RESET}")
    else:
        print(f"[{logtime(0)}] {CYAN}TSDM打工 - 未知原因失败{RESET}")


def tsdm_work_timer():
    while True:
        # 间隔6-7小时
        random_time = random.randint(21600, 21700)

        # 开始打工
        tsdm_work()
        print(f"[{logtime(0)}] {CYAN}TSDM打工{RESET} - 下次将于{logtime(random_time)}开始")
        time.sleep(random_time)
