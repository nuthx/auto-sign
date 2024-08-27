from src.cookie import get_cookie
from src.general import forum_visit


if __name__ == '__main__':
    forum_visit.do({
        "name": "恩山",
        "cookie": get_cookie("right"),
        "url": "https://www.right.com.cn/forum"
    })
