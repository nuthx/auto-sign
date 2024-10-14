from src.cookie import get_cookie
from src.special import skland


if __name__ == '__main__':
    skland.sign({
        "token": get_cookie("skland", "token", main=False)
    })
