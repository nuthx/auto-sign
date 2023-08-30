import time
import random
import requests
from bs4 import BeautifulSoup
from components.function import *


home_url = "https://www.skyey2.com/forum.php"
subtitle_url = "https://www.skyey2.com/forum.php?mod=forumdisplay&fid=75"
download_url = "https://www.skyey2.com/download.php?type=zip&id=37068&name_mod=19"


def skyey_sign():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "cookie": get_cookies("skyey"),
        "connection": "Keep-Alive",
        "x-requested-with": "XMLHttpRequest",
        "referer": home_url,
        "content-type": "application/x-www-form-urlencoded"
    }

    # 打开字幕区
    print(f"[{logtime(0)}] {BLUE}天雪签到{RESET} - 开始")
    response = requests.get(subtitle_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # # 获取字幕区帖子列表
    # result_posts = soup.select("tbody[id^='normalthread_'] .new a:nth-child(3)")
    # posts = []
    # for post in result_posts:
    #     href = post.get("href")
    #     full_url = home_url + href
    #     posts.append(full_url)
    #
    # # 获取前三个帖子
    # for post in posts[:3]:
    #     response = requests.get(subtitle_url, headers=headers)
    #     print(post)

    response = requests.get(download_url, headers=headers)
    with open("lol.zip", "wb") as file:
        file.write(response.content)
    print(response)














    # coin = soup.select_one("#extcreditmenu").text.replace("Gold:", "").strip()
    # print(coin)

    # total_num = soup.select_one("div.bw0 table tr:nth-child(2) td:nth-child(2)").text
    # cycle_num = soup.select_one("div.bw0 table tr:nth-child(2) td:nth-child(3)").text
    # print(f"[{logtime(0)}] {YELLOW}Chiphell签到 - 累计签到{total_num}次，已循环{cycle_num}个周期{RESET}")


def skyey_sign_timer():
    while True:
        # 间隔24小时以上
        random_time = random.randint(86400, 87000)

        # 开始签到
        skyey_sign()
        print(f"[{logtime(0)}] {BLUE}天雪签到{RESET} - 下次将于{logtime(random_time)}开始")
        time.sleep(random_time)
