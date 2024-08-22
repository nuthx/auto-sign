from src.cookie import get_cookie
from src.general import forum_download


if __name__ == '__main__':
    forum_download.do({
        "name": "天雪",
        "cookie": get_cookie("skyey"),
        "url": "https://www.skyey2.com",
        "fid": "16"
    })
