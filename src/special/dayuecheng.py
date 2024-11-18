import requests


def do(forum):
    TOKEN = forum["token"]

    if not TOKEN:
        print("静安大悦城(1/1) - 缺少配置文件，跳过")
        print("——————————")
        return

    headers = {
        "content-type": "application/json;charset=UTF-8"
    }
    json = {
        "MallID": 10024,
        "Header": {
            "Token": TOKEN
        }
    }

    try:
        # 执行签到
        print(f"静安大悦城(1/2) - 签到开始")
        response = requests.post("https://m.mallcoo.cn/api/user/User/CheckinV2", headers=headers, json=json).json()

        # 获取签到的返回信息
        if "已签到过" in response["d"]["Msg"]:
            print(f"静安大悦城(2/2) - 今天已经签过了")
            print("——————————")

        # 获取论坛积分
        else:
            message = response["d"]["Msg"]

            # 输出日志
            print(f"静安大悦城(2/2) - {message}")
            print("——————————")

    except Exception as e:
        print(f"静安大悦城(2/2) - 签到失败，原因：{e}")
        print("——————————")
