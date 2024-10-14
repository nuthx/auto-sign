import requests
from bs4 import BeautifulSoup


def get_coin(url, headers):
    response = requests.get(url + "/home.php?mod=spacecp&ac=credit&op=base", headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    try:
        coin_1 = soup.select_one(".creditl li").text.split(":")
        name_1 = coin_1[0].strip()
        value_1 = coin_1[1].strip().split(" ")[0]  # 再分割一次，避免跟随多个内容
        comb_1 = name_1 + ": " + value_1

        coin_2 = soup.select_one(".creditl li:nth-child(2)").text.split(":")
        name_2 = coin_2[0].strip()
        value_2 = coin_2[1].strip().split(" ")[0]  # 再分割一次，避免跟随多个内容
        comb_2 = name_2 + ": " + value_2

        return comb_1, comb_2

    except Exception as e:
        return


def get_coin_wp(url, headers):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    try:
        coin = soup.select_one("#wp-admin-bar-mycred-account-default li div").text.split(":")
        name = coin[0].strip()
        value = coin[1].strip().split(" ")[0]  # 再分割一次，避免跟随多个内容
        comb = name + ": " + value

        return comb

    except Exception as e:
        return
