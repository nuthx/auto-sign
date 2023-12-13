import re
import time
import requests
from bs4 import BeautifulSoup
from src.function import *


def do(forum):
    name = forum["name"]
    name_cn = forum["name_cn"]

    cookies = get_cookies(name.lower())

    if cookies == 404:
        return

    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "cookie": cookies,
        "referer": forum["subtitle_url"]
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
        "cookie": cookies,
        "Referer": forum["subtitle_url"]
    }

    # 打开字幕区
    log(f"{name_cn}(1/4) - 开始下载字幕")
    response = requests.get(forum["subtitle_url"], headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # 获取字幕区帖子列表
    log(f"{name_cn}(2/4) - 获取帖子列表")
    result_posts = soup.select("tbody[id^='normalthread_'] .s")
    posts = []
    for post in result_posts:
        href = post.get("href")
        full_url = forum["home_url"] + href
        posts.append(full_url)

    # 获取前三个帖子的字幕文件并模拟下载
    i = 1
    for post in posts[:3]:
        response = requests.get(post, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        download_link = soup.select_one("#filelistn + div a").get("href")
        download_link_full = forum["home_url"] + download_link

        # 模拟下载
        requests.get(download_link_full, headers=headers_zip)
        log(f"{name_cn}(3/4) - 下载第{i}个字幕")
        time.sleep(2)
        i += 1

    # 获取论坛积分
    response = requests.get(forum["coin_url"], headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    coin_1 = soup.select_one(".creditl .cl").text.split(":")
    name_1 = coin_1[0].strip()
    value_1 = int(re.sub(r'\D', '', coin_1[1]))

    # 写入csv
    write_csv(name, name_1, value_1, 0, 0)

    # 输出日志
    log(f"{name_cn}(4/4) - {name_1}: {value_1}")
    log("———————————————————————————————————————")
