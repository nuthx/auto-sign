import threading
from components import tsdm, chiphell, skyey


if __name__ == '__main__':
    # tsdm_sign_thread = threading.Thread(target=tsdm.tsdm_sign_timer)
    # tsdm_sign_thread.start()
    #
    # tsdm_work_thread = threading.Thread(target=tsdm.tsdm_work_timer)
    # tsdm_work_thread.start()
    #
    # chiphell_sign_thread = threading.Thread(target=chiphell.chiphell_sign_timer)
    # chiphell_sign_thread.start()

    skyey_sign_thread = threading.Thread(target=skyey.skyey_sign_timer)
    skyey_sign_thread.start()
