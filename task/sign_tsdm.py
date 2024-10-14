from src.cookie import get_cookie
from src.general import forum_sign


if __name__ == '__main__':
    forum_sign.do({
        "name": "天使动漫",
        "cookie": get_cookie("tsdm", main=False),
        "url": "https://www.tsdm39.com"
    })
