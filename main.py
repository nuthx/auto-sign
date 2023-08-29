import time
import datetime
import random
import threading
from components import tsdm, chiphell


def tsdm_sign_timer():
    while True:
        random_time = random.randint(82800, 86400)  # 间隔23-24小时
        next_timestamp = time.time() + random_time
        next_time = datetime.datetime.fromtimestamp(int(next_timestamp))

        tsdm.tsdm_sign()
        print(f"下次签到时间{next_time}")
        time.sleep(random_time)


def tsdm_work_timer():
    while True:
        random_time = random.randint(21600, 21700)  # 间隔23-24小时
        next_timestamp = time.time() + random_time
        next_time = datetime.datetime.fromtimestamp(int(next_timestamp))

        tsdm.tsdm_work()
        print(f"下次打工时间{next_time}")
        time.sleep(random_time)


if __name__ == '__main__':
    tsdm_sign_thread = threading.Thread(target=tsdm_sign_timer)
    tsdm_sign_thread.start()

    tsdm_work_thread = threading.Thread(target=tsdm_work_timer)
    tsdm_work_thread.start()

    chiphell.chiphell_sign_timer()
