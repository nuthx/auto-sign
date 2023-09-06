import time
import random
import requests
from bs4 import BeautifulSoup
from components.function import *


home_url = "https://www.skyey2.com/"
subtitle_url = "https://www.skyey2.com/forum.php?mod=forumdisplay&fid=75"
coin_url = "https://www.skyey2.com/home.php?mod=spacecp&ac=credit&showcredit=1"


def skyey_download():
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "cookie": get_cookies("skyey"),
        "referer": subtitle_url
    }

    headers_zip = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,"
                  "application/signed-exchange;v=b3;q=0.7",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "Dnt": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "cookie": get_cookies("skyey"),
        "Referer": subtitle_url
    }

    # 打开字幕区
    print(f"[{logtime(0)}] {BLUE}天雪(1/4){RESET} - 字幕下载开始")
    response = requests.get(subtitle_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # 获取字幕区帖子列表
    result_posts = soup.select("tbody[id^='normalthread_'] .new a:nth-child(3)")
    posts = []
    for post in result_posts:
        href = post.get("href")
        full_url = home_url + href
        posts.append(full_url)

    # 获取前三个帖子的字幕文件并模拟下载
    i = 1
    for post in posts[:3]:
        response = requests.get(post, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        download_link = soup.select_one("#filelistn + div a").get("href")
        download_link_full = home_url + download_link

        # 模拟下载
        requests.get(download_link_full, headers=headers_zip)
        print(f"[{logtime(0)}] {BLUE}天雪(2/4){RESET} - 模拟下载第{i}个字幕")
        time.sleep(2)
        i += 1

    # 获取当前积分数
    response = requests.post(coin_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    credit = soup.select_one(".creditl .cl").text[:10].replace("金币:", "").strip()
    print(f"[{logtime(0)}] {BLUE}天雪(3/4){RESET} - 当前拥有{credit}金币")


def skyey_download_timer():
    while True:
        # 间隔24小时以上
        random_time = random.randint(86400, 87000)

        # 开始签到
        skyey_download()
        print(f"[{logtime(0)}] {BLUE}天雪(4/4){RESET} - 下次将于{logtime(random_time)}再次下载")
        print(f"[{logtime(0)}] ———————————————————————————————————————————————")
        time.sleep(random_time)
