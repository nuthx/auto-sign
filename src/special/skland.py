# 参考代码：https://gitee.com/FancyCabbage/skyland-auto-sign

import json
import time
import requests
import hmac
import hashlib

from urllib import parse
from ast import literal_eval


header = {
    'cred': '',
    'User-Agent': 'Skland/1.0.1 (com.hypergryph.skland; build:100001014; Android 31; ) Okhttp/4.11.0',
    'Accept-Encoding': 'gzip',
    'Connection': 'close'
}
header_printin = {
    'User-Agent': 'Skland/1.0.1 (com.hypergryph.skland; build:100001014; Android 31; ) Okhttp/4.11.0',
    'Accept-Encoding': 'gzip',
    'Connection': 'close'
}

# 签名请求头一定要这个顺序，否则失败
# timestamp是必填的,其它三个随便填,不要为none即可
header_for_sign = {
    'platform': '',
    'timestamp': '',
    'dId': '',
    'vName': ''
}

# 签到url
sign_url = "https://zonai.skland.com/api/v1/game/attendance"
# 绑定的角色url
binding_url = "https://zonai.skland.com/api/v1/game/player/binding"
# 使用token获得认证代码
grant_code_url = "https://as.hypergryph.com/user/oauth2/v2/grant"
# 使用认证代码获得cred
cred_code_url = "https://zonai.skland.com/api/v1/user/auth/generate_cred_by_code"


def generate_signature(token: str, path, body_or_query):
    """
    获得签名头
    接口地址+方法为Get请求？用query否则用body+时间戳+ 请求头的四个重要参数（dId，platform，timestamp，vName）.toJSON()
    将此字符串做HMAC加密，算法为SHA-256，密钥token为请求cred接口会返回的一个token值
    再将加密后的字符串做MD5即得到sign
    param token: 拿cred时候的token
    param path: 请求路径（不包括网址）
    param body_or_query: 如果是GET，则是它的query。POST则为它的body
    return: 计算完毕的sign
    """

    t = str(int(time.time()) - 2)
    token = token.encode('utf-8')
    header_ca = json.loads(json.dumps(header_for_sign))
    header_ca['timestamp'] = t
    header_ca_str = json.dumps(header_ca, separators=(',', ':'))
    s = path + body_or_query + t + header_ca_str
    hex_s = hmac.new(token, s.encode('utf-8'), hashlib.sha256).hexdigest()
    md5 = hashlib.md5(hex_s.encode('utf-8')).hexdigest().encode('utf-8').decode('utf-8')
    # printging.info(f'算出签名: {md5}')
    return md5, header_ca


def get_sign_header(url: str, method, body, old_header):
    h = json.loads(json.dumps(old_header))
    p = parse.urlparse(url)
    if method.lower() == 'get':
        h['sign'], header_ca = generate_signature(sign_token, p.path, p.query)
    else:
        h['sign'], header_ca = generate_signature(sign_token, p.path, json.dumps(body))
    for i in header_ca:
        h[i] = header_ca[i]
    return h


def get_cred_by_token(token):
    grant_code = get_grant_code(token)
    return get_cred(grant_code)


def get_grant_code(token):
    response = requests.post(grant_code_url, json={
        'appCode': '4ca99fa6b56cc2ba',
        'token': token,
        'type': 0
    }, headers=header_printin)
    resp = response.json()
    if response.status_code != 200:
        raise Exception(f'获得认证代码失败：{resp}')
    if resp.get('status') != 0:
        raise Exception(f'获得认证代码失败：{resp["msg"]}')
    return resp['data']['code']


def get_cred(grant):
    resp = requests.post(cred_code_url, json={
        'code': grant,
        'kind': 1
    }, headers=header_printin).json()
    if resp['code'] != 0:
        raise Exception(f'获得cred失败：{resp["message"]}')
    return resp['data']


def get_uid():
    resp = requests.get(binding_url, headers=get_sign_header(binding_url, 'get', None, header)).json()
    uid = resp['data']['list'][0]['bindingList'][0]['uid']
    return uid


def sign(forum):
    token_list = forum["token"]

    if not token_list:
        print("明日方舟(1/1) - 缺少配置文件，跳过")
        return

    # 多账号支持
    for token in literal_eval(token_list):  # 转为数组
        index = token.index(token)
        print(f"明日方舟 账号{index + 1}(1/2) - 签到开始")

        # 开始签到
        global sign_token
        cred_resp = get_cred_by_token(token)
        sign_token = cred_resp['token']
        header['cred'] = cred_resp['cred']
        body = {'gameId': 1, 'uid': get_uid()}
        result = requests.post(sign_url, headers=get_sign_header(sign_url, 'post', body, header), json=body).json()

        # 获取签到返回内容
        if result["message"] == "OK":
            award_name = result["data"]["awards"][0]["resource"]["name"]
            award_count = result["data"]["awards"][0]["count"]
            print(f"明日方舟 账号{index + 1}(2/2) - 获得了{award_name} x{award_count}")
        else:
            print(f"明日方舟 账号{index + 1}(2/2) - {result['message']}")
