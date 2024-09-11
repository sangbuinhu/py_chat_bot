from src.config import constants
from src.services.evn import check_ma_khach_hang
from src.telegram import telegram_bot
from src.utils import log_util
from src.utils.date_util import extract_dates_from_text, compare_with_today


def check_cup_dien(event, context):
    try:
        for key, value in constants.LIST_MA_KH.items():
            print(key, value)
            result_no, results_info = check_ma_khach_hang(key, value)
            for result in results_info:
                result_text = result.get_text()
                if result_text:
                    # Extract dates from the example text
                    dates = extract_dates_from_text(result_text)
                    if compare_with_today(dates[1]):
                        message_content = "---------------------------------------------\n" \
                                          + result_no \
                                          + "\n" \
                                          + "---------------------------------------------" \
                                          + result_text
                        telegram_bot.send_message(constants.TELEGRAM_MSG_FROM_ID, message_content)
                        print(f"SENT MESSAGE {result_no}")
                else:
                    print("KHÔNG CÓ LỊCH CÚP ĐIỆN: " + value)
    except Exception as e:
        log_util.show_log(e)


check_cup_dien("", "")
