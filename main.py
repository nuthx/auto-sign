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
    log("自动签到启动 20231214")
    log("———————————————————————————————————————")

    # 访问
    chiphell = every_second(random.randint(86401, 86500), task.chiphell_visit)
    vcb = every_day(random_time("08:00"), task.vcb_visit)

    # 打工
    tsdm_1 = every_second(random.randint(21601, 21700), task.tsdm_work)

    # 签到
    tsdm_2 = every_day(random_time("08:10"), task.tsdm_sign)
    sayhuahuo = every_day(random_time("08:20"), task.sayhuahuo_sign)

    # 签到Plus
    sksj = every_day(random_time("08:30"), task.sksj_sign)

    # 字幕下载
    skyey = every_day(random_time("08:40"), task.skyey_download)

    # 游戏签到
    skland = every_day(random_time("08:50"), task.skland_sign)

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
