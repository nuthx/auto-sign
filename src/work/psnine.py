import time
import requests
from bs4 import BeautifulSoup
from src.function import *


def do():
    # 获取配置中的cookies
    config = configparser.ConfigParser()
    config.read(os.path.join("config", "config.ini"))

    psnid = config.get("psnine", "psnid")
    shell = config.get("psnine", "shell")

    # 请求信息
    url = "https://psnine.com/set/qidao/ajax"

    cookie = f"__Psnine_psnid={psnid}; __Psnine_shell={shell}; __Psnine_qidaodate={int(time.time())}"

    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "cookie": cookie,
    }

    # 是否存在配置信息，如果不存在则跳过
    if "" in (psnid, shell):
        print(f"缺少PSNINE配置，跳过")
        print("———————————————————————————————————————")
        return

    # 执行签到
    print(f"PSNINE(1/2) - 签到开始")
    response = requests.get(url, headers=headers)

    # 获取签到的返回信息
    if "已经签过" in response.text:
        print(f"PSNINE(2/2) - 今天已经签过了")
        print("———————————————————————————————————————")

    # 获取论坛积分
    else:
        soup = BeautifulSoup(response.text, 'html.parser')
        day = soup.select_one("div b:nth-child(5)").text

        # 输出日志
        print(f"PSNINE(2/2) - 已祈祷{day}天")
        print("———————————————————————————————————————")
