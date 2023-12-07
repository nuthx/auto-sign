import time
import schedule
from src import task
from src.function import *


def every_day(j_time, j_name):
    scheduler = schedule.Scheduler()
    scheduler.every().day.at(j_time).do(j_name)
    return scheduler


def every_second(j_time, j_name):
    scheduler = schedule.Scheduler()
    scheduler.every(j_time).seconds.do(j_name)
    return scheduler


if __name__ == '__main__':
    log("———————————————————————————————————————")
    log("自动签到启动 20231207")
    log("———————————————————————————————————————")

    chiphell = every_second(86450, task.chiphell_visit)
    vcb = every_day("08:32:15", task.vcb_visit)

    tsdm_1 = every_second(21650, task.tsdm_work)

    tsdm_2 = every_day("09:24:19", task.tsdm_sign)
    sayhuahuo = every_day("10:16:43", task.sayhuahuo_sign)

    sksj = every_day("11:07:21", task.sksj_sign)

    skyey = every_day("12:55:37", task.skyey_download)

    skland = every_day("13:42:08", task.skland_sign)

    while True:
        chiphell.run_pending()
        vcb.run_pending()
        tsdm_1.run_pending()
        tsdm_2.run_pending()
        sayhuahuo.run_pending()
        sksj.run_pending()
        skyey.run_pending()
        skland.run_pending()
        time.sleep(1)
