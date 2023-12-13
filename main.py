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
    log("自动签到启动 20231213")
    log("———————————————————————————————————————")

    chiphell = every_second(86450, task.chiphell_visit)
    vcb = every_day("08:02:15", task.vcb_visit)

    tsdm_1 = every_second(21650, task.tsdm_work)

    tsdm_2 = every_day("08:14:19", task.tsdm_sign)
    sayhuahuo = every_day("08:26:43", task.sayhuahuo_sign)

    sksj = every_day("08:37:21", task.sksj_sign)

    skyey = every_day("08:45:37", task.skyey_download)

    skland = every_day("08:57:08", task.skland_sign)

    # 启动时执行一次所有任务
    task.chiphell_visit()
    task.vcb_visit()
    task.tsdm_work()
    task.tsdm_sign()
    task.sayhuahuo_sign()
    task.sksj_sign()
    task.skyey_download()
    task.skland_sign()

    # 每日任务
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
