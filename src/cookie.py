import os
import configparser


def get_cookie(name, category="forum"):
    # 加载青龙的环境变量
    ql_env = category + "_" + name
    if os.environ.get(ql_env):
        return os.environ.get(ql_env)

    # 加载本地配置文件
    else:
        config = configparser.ConfigParser(interpolation=None)  # 避免%被解析

        if os.path.exists("config/config.ini"):
            config.read("config/config.ini")
            return config.get(category, name)
        else:
            config.read("../config/config.ini")
            return config.get(category, name)
