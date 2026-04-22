"""Telegram bot utilities for sending messages via the Bot API."""

import requests

from src.config import constants
from src.utils import log_util


def send_message(chat_id: str, message: str) -> bool:
    """Send a text message to a Telegram chat.

    Args:
        chat_id: The target chat or user ID.
        message: The text content to send.

    Returns:
        True if the message was sent successfully, False otherwise.
    """
    try:
        url = f"{constants.TELEGRAM_BOT_BASE_URL}/sendMessage"
        payload = {"chat_id": chat_id, "text": message}
        response = requests.post(url, json=payload, timeout=10)
        response.raise_for_status()
        return True
    except requests.RequestException as e:
        log_util.show_log(e)
        return False
