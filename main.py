import time
import threading
from components import tsdm, chiphell, skyey, sayhuahuo, siksj, skland


if __name__ == '__main__':
    run_timer = [
        tsdm.tsdm_sign_timer,
        tsdm.tsdm_work_timer,
        chiphell.chiphell_sign_timer,
        skyey.skyey_download_timer,
        sayhuahuo.sayhuahuo_sign_timer,
        siksj.siksj_sign_timer,
        skland.skland_sign_timer,
        skland.skland_apcheck_timer,
    ]

    for timer in run_timer:
        thread = threading.Thread(target=timer)
        thread.start()
        time.sleep(8)
