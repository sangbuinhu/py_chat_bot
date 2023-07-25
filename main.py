from src.config import constants
from src.messenger import messenger
from src.power_outage import power_outage
from src.utils import log_util


def check_cup_dien(event, context):
    try:
        for key, value in constants.LIST_MA_KH.items():
            print(key, value)
            result = power_outage.check_ma_khach_hang(key, value)
            if result:
                messenger.send_message(
                    constants.PAGE_ACCESS_TOKEN,
                    constants.RECIPIENT_ID,
                    result
                )
            else:
                print("KHÔNG CÓ LỊCH CÚP ĐIỆN: " + value)
    except Exception as e:
        log_util.show_log(e)
