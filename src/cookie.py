import json


def get_cookie(name, category="cookie"):
    with open("config/config.json", 'r', encoding='utf-8') as file:
        config = json.load(file)

    return config[name][category]
