from src.work import forum_visit


def chiphell_visit():
    forum_visit.do({
        "name": "Chiphell",
        "coin_type": 1,
        "home_url": "https://www.chiphell.com/forum.php",
        "credit_url": "https://www.chiphell.com/home.php?mod=spacecp&ac=credit&op=base"
    })


def vcb_visit():
    forum_visit.do({
        "name": "VCB",
        "coin_type": 2,
        "home_url": "https://bbs.acgrip.com/",
        "credit_url": "https://bbs.acgrip.com/home.php?mod=spacecp&ac=credit&op=base"
    })
