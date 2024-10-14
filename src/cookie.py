import json


def get_cookie(name, category="cookie", main=True):
    if main:
        file_path = "config/config.json"
    else:
        file_path = "../config/config.json"

    with open(file_path, 'r', encoding='utf-8') as file:
        config = json.load(file)

    return config[name][category]
