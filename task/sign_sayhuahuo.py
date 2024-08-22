from src.cookie import get_cookie
from src.general import forum_sign


if __name__ == '__main__':
    forum_sign.do({
        "name": "花火学园",
        "cookie": get_cookie("sayhuahuo"),
        "url": "https://www.sayhuahuo.net"
    })
