import time
import threading
from components.function import *
from components import tsdm, chiphell, skyey, sayhuahuo, siksj, skland


if __name__ == '__main__':
    version = "1.01"
    auto_sign = '''
                 __                         _           
    ____ ___  __/ /_____              _____(_)___ _____ 
   / __ `/ / / / __/ __ \   ______   / ___/ / __ `/ __ \\
  / /_/ / /_/ / /_/ /_/ /  /_____/  (__  ) / /_/ / / / /
  \__,_/\__,_/\__/\____/           /____/_/\__, /_/ /_/ 
                                          /____/        
    '''

    for line in auto_sign.splitlines():
        print(f"[{logtime(0)}] {line}")
        time.sleep(0.05)

    print(f"[{logtime(0)}] ———————————————————————————————————————————————")
    print(f"[{logtime(0)}] 自动签到程序启动（ver.{version}）")
    print(f"[{logtime(0)}] ———————————————————————————————————————————————")

    run_timer = [
        tsdm.tsdm_sign_timer,
        tsdm.tsdm_work_timer,
        chiphell.chiphell_sign_timer,
        sayhuahuo.sayhuahuo_sign_timer,
        siksj.siksj_sign_timer,
        skland.skland_sign_timer,
        skland.skland_apcheck_timer,
        skyey.skyey_download_timer,
    ]

    for timer in run_timer:
        thread = threading.Thread(target=timer)
        thread.start()
        time.sleep(8)
