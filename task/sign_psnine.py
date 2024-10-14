from src.cookie import get_cookie
from src.special import psnine


if __name__ == '__main__':
    psnine.do({
        "psnid": get_cookie("psnine", "psnid", main=False),
        "shell": get_cookie("psnine", "shell", main=False)
    })
