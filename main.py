"""Entry point for the EVN power outage notification bot."""

# cSpell:disable
from src.config import constants
from src.services.evn import check_ma_khach_hang
from src.telegram import telegram_bot
from src.utils import log_util
from src.utils.date_util import extract_dates_from_text, compare_with_today

SEPARATOR = "---------------------------------------------"


def check_cup_dien(event, context):
    """Check power outage schedules and notify via Telegram.

    Iterates over all configured customer codes, fetches their outage schedule,
    and sends a Telegram message for any upcoming outage.

    Args:
        event: Cloud function event payload (unused).
        context: Cloud function context (unused).
    """
    try:
        for ma_kh, ten_kh in constants.LIST_MA_KH.items():
            telegram_bot.send_message(constants.TELEGRAM_MSG_FROM_ID, "message_content")
            result = check_ma_khach_hang(ma_kh, ten_kh)
            if result is None:
                log_util.show_log(Exception(f"Failed to fetch schedule for {ten_kh}"))
                continue

            result_no, results_info = result
            has_schedule = False

            for item in results_info:
                result_text = item.get_text()
                if not result_text:
                    continue

                dates = extract_dates_from_text(result_text)
                if len(dates) < 2:
                    continue

                if compare_with_today(dates[1]):
                    has_schedule = True
                    message_content = (
                        f"{SEPARATOR}\n{result_no}\n{SEPARATOR}\n{result_text}"
                    )
                    telegram_bot.send_message(
                        constants.TELEGRAM_MSG_FROM_ID, message_content
                    )
                    print(f"SENT MESSAGE {result_no}")

            if not has_schedule:
                print(f"KHÔNG CÓ LỊCH CÚP ĐIỆN: {ten_kh}")

    except (KeyError, ValueError, AttributeError) as e:
        log_util.show_log(e)


if __name__ == "__main__":
    check_cup_dien("", "")
