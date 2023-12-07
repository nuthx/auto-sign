from src.work import forum_visit, forum_work, forum_sign, forum_sign_plus, forum_download, skland
from src.function import *


def chiphell_visit():
    try:
        forum_visit.do({
            "name": "Chiphell",
            "home_url": "https://www.chiphell.com/forum.php",
            "coin_url": "https://www.chiphell.com/home.php?mod=spacecp&ac=credit&op=base"
        })
    except Exception as e:
        log(e)
        log("———————————————————————————————————————")


def vcb_visit():
    try:
        forum_visit.do({
            "name": "VCB",
            "home_url": "https://bbs.acgrip.com/",
            "coin_url": "https://bbs.acgrip.com/home.php?mod=spacecp&ac=credit&op=base"
        })
    except Exception as e:
        log(e)
        log("———————————————————————————————————————")


def tsdm_work():
    try:
        forum_work.do({
            "name": "tsdm",
            "name_cn": "天使动漫",
            "sign_url": "https://www.tsdm39.com/plugin.php?id=dsu_paulsign:sign",
            "work_url": "https://www.tsdm39.com/plugin.php?id=np_cliworkdz:work",
            "coin_url": "https://www.tsdm39.com/home.php?mod=spacecp&ac=credit&showcredit=1"
        })
    except Exception as e:
        log(e)
        log("———————————————————————————————————————")


def tsdm_sign():
    try:
        forum_sign.do({
            "name": "tsdm",
            "name_cn": "天使动漫",
            "sign_url": "https://www.tsdm39.com/plugin.php?id=dsu_paulsign:sign",
            "sign_post": "https://www.tsdm39.com/plugin.php?id=dsu_paulsign:sign&operation=qiandao&infloat=1&inajax=1",
            "coin_url": "https://www.tsdm39.com/home.php?mod=spacecp&ac=credit&showcredit=1"
        })
    except Exception as e:
        log(e)
        log("———————————————————————————————————————")


def sayhuahuo_sign():
    try:
        forum_sign.do({
            "name": "sayhuahuo",
            "name_cn": "花火学园",
            "sign_url": "https://www.sayhuahuo.net/dsu_paulsign-sign.html",
            "sign_post": "https://www.sayhuahuo.net/plugin.php?id=dsu_paulsign:sign&operation=qiandao&infloat=1&inajax=1",
            "coin_url": "https://www.sayhuahuo.net/home.php?mod=spacecp&ac=credit&showcredit=1"
        })
    except Exception as e:
        log(e)
        log("———————————————————————————————————————")


def sksj_sign():
    try:
        forum_sign_plus.do({
            "name": "sksj",
            "name_cn": "4K世界",
            "sign_url": "https://www.4ksj.com/qiandao/",
            "sign_post": "https://www.4ksj.com/qiandao/?mod=sign&operation=qiandao&format=empty&inajax=1&ajaxtarget=",
            "coin_url": "https://www.4ksj.com/home.php?mod=spacecp&ac=credit"
        })
    except Exception as e:
        log(e)
        log("———————————————————————————————————————")


def skyey_download():
    try:
        forum_download.do({
            "name": "skyey",
            "name_cn": "天雪",
            "home_url": "https://www.skyey2.com/",
            "subtitle_url": "https://www.skyey2.com/forum.php?mod=forumdisplay&fid=75",
            "coin_url": "https://www.skyey2.com/home.php?mod=spacecp&ac=credit&showcredit=1"
        })
    except Exception as e:
        log(e)
        log("———————————————————————————————————————")


def skland_sign():
    try:
        skland.sign()
    except Exception as e:
        log(e)
        log("———————————————————————————————————————")
