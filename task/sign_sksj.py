from src.cookie import get_cookie
from src.general import forum_sign_plus


if __name__ == '__main__':
    forum_sign_plus.do({
        "name": "4K世界",
        "cookie": get_cookie("sksj", main=False),
        "url": "https://www.4ksj.com"
    })
