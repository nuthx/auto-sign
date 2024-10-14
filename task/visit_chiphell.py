from src.cookie import get_cookie
from src.general import forum_visit


if __name__ == '__main__':
    forum_visit.do({
        "name": "Chiphell",
        "cookie": get_cookie("chiphell", main=False),
        "url": "https://www.chiphell.com"
    })
