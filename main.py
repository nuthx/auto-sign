import time
import schedule
from src import task
from src.function import *


def set_time(j_time, j_name):
    scheduler = schedule.Scheduler()
    scheduler.every().day.at(j_time).do(j_name)
    return scheduler


if __name__ == '__main__':
    log("———————————————————————————————————————")
    log("自动签到启动 20231205")
    log("———————————————————————————————————————")

    # task.chiphell_visit()
    # task.vcb_visit()

    # task.tsdm_work()

    # task.tsdm_sign()
    # task.sayhuahuo_sign()

    task.sksj_sign()

    # task.skyey_download()




    chiphell = set_time("10:58:00", task.chiphell_visit)
    vcb = set_time("10:58:00", task.vcb_visit)

    while True:
        chiphell.run_pending()
        vcb.run_pending()
        time.sleep(1)
