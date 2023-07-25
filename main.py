import time

from config import constants
from src.messenger import messenger
from src.power_outage import power_outage
from utils import log_util


def check_cup_dien():
    try:
        for ma_kh in constants.LIST_MA_KH:
            result = power_outage.check_ma_khach_hang(ma_kh)
            if result:
                messenger.send_message(
                    constants.PAGE_ACCESS_TOKEN,
                    constants.RECIPIENT_ID,
                    result
                )
    except Exception as e:
        log_util.show_log(e)


if __name__ == "__main__":
    # Infinite loop to run the function repeatedly
    while True:
        check_cup_dien()
        time.sleep(constants.DELAY_IN_SECONDS)
