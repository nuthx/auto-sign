import time
import random
import requests
from bs4 import BeautifulSoup
from components.function import *


home_url = "https://www.tsdm39.com/forum.php"
sign_url = "https://www.tsdm39.com/plugin.php?id=dsu_paulsign:sign"
sign_post = "https://www.tsdm39.com/plugin.php?id=dsu_paulsign:sign&operation=qiandao&infloat=1&inajax=1"
work_url = "https://www.tsdm39.com/plugin.php?id=np_cliworkdz:work"
coin_url = "https://www.tsdm39.com/home.php?mod=spacecp&ac=credit&showcredit=1"


def tsdm_sign():
    # 必须要这个content-type, 否则没法接收
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "cookie": get_cookies("tsdm"),
        "referer": sign_url
    }

    # 获取formhash
    print(f"[{logtime(0)}] {MAGENTA}天使动漫(1/4){RESET} - 签到开始")
    response = requests.post(sign_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    formhash = soup.select_one("#scbar_form input:nth-child(2)").get("value")

    # 执行签到
    sign_data = "formhash=" + formhash + "&qdxq=wl&qdmode=3&todaysay=&fastreply=1"
    response = requests.post(sign_post, data=sign_data, headers=headers)

    # 获取签到的返回信息
    soup_xml = BeautifulSoup(response.text, "xml")
    soup_html = BeautifulSoup(soup_xml.root.string, 'html.parser')
    sign_result = soup_html.select_one(".c").text.replace(".", "").strip()
    print(f"[{logtime(0)}] {MAGENTA}天使动漫(2/4){RESET} - " + sign_result)

    # 获取当前积分数
    response = requests.post(coin_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    credit = soup.select_one(".creditl li").text.replace("天使币:", "").strip()
    print(f"[{logtime(0)}] {MAGENTA}天使动漫(3/4){RESET} - 当前拥有{credit}天使币")


def tsdm_sign_timer():
    while True:
        # 间隔24小时以上
        random_time = random.randint(86400, 87000)

        # 开始签到
        tsdm_sign()
        print(f"[{logtime(0)}] {MAGENTA}天使动漫(4/4){RESET} - 下次将于{logtime(random_time)}开始签到")
        time.sleep(random_time)


def tsdm_work():
    # 必须要这个content-type, 否则没法接收
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "cookie": get_cookies("tsdm"),
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
