import time
import requests
from bs4 import BeautifulSoup

from src.coin import get_coin


def do(forum):
    NAME = forum["name"]
    COOKIE = forum["cookie"]
    URL = forum["url"]
    FID = forum["fid"]

    if not COOKIE:
        print(f"{NAME}(1/1) - 缺少配置文件，跳过")
        print("——————————")
        return

    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "cookie": COOKIE,
        "referer": URL + "/forum.php?mod=forumdisplay&fid=" + FID
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
        "cookie": COOKIE,
        "referer": URL + "/forum.php?mod=forumdisplay&fid=" + FID
    }

    try:
        # 打开dif对应字幕区
        print(f"{NAME}(1/4) - 开始下载字幕")
        response = requests.get(URL + "/forum.php?mod=forumdisplay&fid=" + FID, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        # 获取帖子列表
        print(f"{NAME}(2/4) - 获取帖子列表")
        result_posts = soup.select("tbody[id^='normalthread_'] .s")
        posts = []
        for post in result_posts:
            href = post.get("href")
            full_url = URL + "/" + href
            posts.append(full_url)

        # 获取前三个帖子的字幕文件并模拟下载
        i = 1
        for post in posts[:3]:
            response = requests.get(post, headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')
            download_link = soup.select_one("#filelistn + div a").get("href")

            # 模拟下载
            requests.get(URL + "/" + download_link, headers=headers_zip)
            print(f"{NAME}(3/4) - 下载第{i}个字幕")
            time.sleep(2)
            i += 1

        # 获取论坛积分
        coin = get_coin(URL, headers)
        if coin:
            print(f"{NAME}(3/3) - {coin[0]}, {coin[1]}")
            print("——————————")
        else:
            print(f"{NAME}(3/3) - 余额获取失败")
            print("——————————")

    except Exception as e:
        print(f"{NAME}(3/3) - 下载失败，原因：{e}")
        print("——————————")
