import time
import requests
from bs4 import BeautifulSoup


def do(forum):
    PSNID = forum["psnid"]
    SHELL = forum["shell"]

    if not PSNID or not SHELL:
        print("PSNINE(1/1) - 缺少配置文件，跳过")
        print("——————————")
        return

    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "cookie": f"__Psnine_psnid={PSNID}; __Psnine_shell={SHELL}; __Psnine_qidaodate={int(time.time())}",
    }

    # 执行签到
    print(f"PSNINE(1/2) - 签到开始")
    response = requests.get("https://psnine.com/set/qidao/ajax", headers=headers)

    # 获取签到的返回信息
    if "已经签过" in response.text:
        print(f"PSNINE(2/2) - 今天已经签过了")
        print("——————————")

    # 获取论坛积分
    else:
        soup = BeautifulSoup(response.text, 'html.parser')
        day = soup.select_one("div b:nth-child(5)").text

        # 输出日志
        print(f"PSNINE(2/2) - 已祈祷{day}天")
        print("——————————")
