from src.cookie import get_cookie
from src.general import forum_work


if __name__ == '__main__':
    print("——————————")

    forum_work.do({
        "name": "天使动漫",
        "cookie": get_cookie("tsdm"),
        "url": "https://www.tsdm39.com"
    })
