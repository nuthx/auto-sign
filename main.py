from src.cookie import get_cookie
from src.general import forum_visit, forum_sign, forum_sign_plus, forum_work, forum_download
from src.special import psnine, skland


if __name__ == '__main__':
    print("——————————")

    forum_visit.do({
        "name": "Chiphell",
        "cookie": get_cookie("chiphell"),
        "url": "https://www.chiphell.com"
    })

    forum_visit.do({
        "name": "VCB",
        "cookie": get_cookie("vcb"),
        "url": "https://bbs.acgrip.com"
    })

    forum_sign.do({
        "name": "天使动漫",
        "cookie": get_cookie("tsdm"),
        "url": "https://www.tsdm39.com"
    })

    forum_work.do({
        "name": "天使动漫",
        "cookie": get_cookie("tsdm"),
        "url": "https://www.tsdm39.com"
    })

    forum_sign.do({
        "name": "花火学园",
        "cookie": get_cookie("sayhuahuo"),
        "url": "https://www.sayhuahuo.net"
    })

    forum_sign_plus.do({
        "name": "4K世界",
        "cookie": get_cookie("sksj"),
        "url": "https://www.4ksj.com"
    })

    forum_visit.do({
        "name": "恩山",
        "cookie": get_cookie("right"),
        "url": "https://www.right.com.cn/forum"
    })

    forum_download.do({
        "name": "天雪",
        "cookie": get_cookie("skyey"),
        "url": "https://www.skyey2.com",
        "fid": "16"
    })

    psnine.do({
        "psnid": get_cookie("psnine", "psnid"),
        "shell": get_cookie("psnine", "shell")
    })

    skland.sign({
        "token": get_cookie("skland", "token")
    })
