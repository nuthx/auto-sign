import time
import threading
from components.function import *
from components import tsdm, chiphell, skyey, sayhuahuo, siksj, skland, vcb


if __name__ == '__main__':
    log("———————————————————————————————————————————————")
    log("自动签到启动 20231121")
    log("———————————————————————————————————————————————")

    run_timer = [
        skland.skland_sign_timer,
        tsdm.tsdm_sign_timer,
        tsdm.tsdm_work_timer,
        chiphell.chiphell_sign_timer,
        sayhuahuo.sayhuahuo_sign_timer,
        # siksj.siksj_sign_timer,
        skyey.skyey_download_timer,
        vcb.vcb_sign_timer,
    ]

    for timer in run_timer:
            thread = threading.Thread(target=timer)
            thread.start()
            time.sleep(12)
