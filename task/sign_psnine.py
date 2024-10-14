from src.cookie import get_cookie
from src.special import psnine


if __name__ == '__main__':
    psnine.do({
        "psnid": get_cookie("psnid", "psnine", main=False),
        "shell": get_cookie("shell", "psnine", main=False)
    })
