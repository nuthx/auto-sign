from src.cookie import get_cookie
from src.general import forum_visit, forum_sign, forum_sign_plus, forum_work, forum_download
from src.special import psnine, skland


if __name__ == '__main__':
    print("——————————")

    # Chiphell
    forum_visit.do({
        "name": "Chiphell",
        "cookie": get_cookie("chiphell"),
        "url": "https://www.chiphell.com"
    })
    print("——————————")

    # VCB
    forum_visit.do({
        "name": "VCB",
        "cookie": get_cookie("vcb"),
        "url": "https://bbs.acgrip.com"
    })
    print("——————————")

    # 天使动漫 - 签到
    forum_sign.do({
        "name": "天使动漫",
        "cookie": get_cookie("tsdm"),
        "url": "https://www.tsdm39.com"
    })
    print("——————————")

    # 天使动漫 - 打工
    forum_work.do({
        "name": "天使动漫",
        "cookie": get_cookie("tsdm"),
        "url": "https://www.tsdm39.com"
    })
    print("——————————")

    # 花火学园
    forum_sign.do({
        "name": "花火学园",
        "cookie": get_cookie("sayhuahuo"),
        "url": "https://www.sayhuahuo.net"
    })
    print("——————————")

    # 4K世界
    forum_sign_plus.do({
        "name": "4K世界",
        "cookie": get_cookie("sksj"),
        "url": "https://www.4ksj.com"
    })
    print("——————————")

    # 恩山
    forum_visit.do({
        "name": "恩山",
        "cookie": get_cookie("right"),
        "url": "https://www.right.com.cn/forum"
    })

    # 天雪
    forum_download.do({
        "name": "天雪",
        "cookie": get_cookie("skyey"),
        "url": "https://www.skyey2.com",
        "fid": "16"
    })
    print("——————————")

    # PSNINE
    psnine.do({
        "psnid": get_cookie("psnine", "psnid"),
        "shell": get_cookie("psnine", "shell")
    })
    print("——————————")

    # 明日方舟
    skland.sign({
        "token": get_cookie("skland", "token")
    })
    print("——————————")
