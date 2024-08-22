from src.cookie import get_cookie
from src.general import forum_visit


if __name__ == '__main__':
    forum_visit.do({
        "name": "VCB",
        "cookie": get_cookie("vcb"),
        "url": "https://bbs.acgrip.com"
    })
