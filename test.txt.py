import requests

url = "https://www.skyey2.com/download.php?type=zip&id=37199&name_mod=19"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "cookie": "rkvl_2132_refreshcollapse4=no; rkvl_2132_smile=10D1; rkvl_2132_nofavfid=1; rkvl_2132_saltkey=iwusohJG; rkvl_2132_lastvisit=1693297487; rkvl_2132_auth=4d63%2FAPoSt3yvD9AK3TqRbPCpS0q8TlHzGOGLp%2BqFmG5vI8%2BnnRA%2F%2F51ZxIhe3hI%2FL9qw505v01fidJq40%2F6sjD9JQ; rkvl_2132_lastcheckfeed=41515%7C1693389166; rkvl_2132_lastcheck=1; rkvl_2132_ulastactivity=9becfiuMePOVKFtpUVz2tr88tk8fXeme2vCgxrsP5iMIpa%2B5Vy1a; rkvl_2132_st_t=41515%7C1693452145%7C3b7930b1a52e230884c41a69eeae7662; rkvl_2132_forum_lastvisit=D_16_1693390582D_8_1693451989D_75_1693452145; rkvl_2132_visitedfid=16D75D8D69D10D36D7; rkvl_2132_sid=XAz5SB; rkvl_2132_lip=103.169.216.19%2C1693452192; rkvl_2132_visitedtid=4810; rkvl_2132_viewid=tid_4810; rkvl_2132_sendmail=1; rkvl_2132_st_p=41515%7C1693452297%7C67da7f69c6223f170a93072d67407891; rkvl_2132_lastact=1693452298%09home.php%09spacecp; rkvl_2132_checkpm=1",
    "Dnt": "1",
    "Referer": "https://www.skyey2.com/forum.php?mod=viewthread&tid=46443",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",

}

response = requests.get(url, headers=headers)

if response.text:
    print(response.text)  # 打印响应内容
else:
    print(0)
