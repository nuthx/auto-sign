from src.cookie import get_cookie
from src.general import wordpress_visit


if __name__ == '__main__':
    wordpress_visit.do({
        "name": "心动日剧",
        "cookie": get_cookie("doki8"),
        "url": "http://www.doki8.net"
    })
