import requests

from src.config import constants
from src.utils import log_util


def send_message(chat_id, message):
    try:
        url = f"{constants.TELEGRAM_BOT_BASE_URL}/sendMessage"
        payload = {
            "chat_id": chat_id,
            "text": message
        }
        headers = {
            "Content-Type": "application/json"
        }

        requests.get(url, json=payload, headers=headers)
    except Exception as e:
        log_util.show_log(e)
