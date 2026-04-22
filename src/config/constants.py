"""Application constants loaded from environment variables."""

import ast
import os

from dotenv import load_dotenv

load_dotenv()

LIST_MA_KH: dict = ast.literal_eval(os.getenv("LIST_MA_KH", "{}"))
DELAY_IN_SECONDS: int = 86400

URL_CHECK_CUP_DIEN: str = os.getenv("URL_CHECK_CUP_DIEN", "")

# Telegram
TELEGRAM_BOT_TOKEN: str = os.getenv("TELEGRAM_CHAT_BOT_TOKEN", "")
TELEGRAM_BOT_BASE_URL: str = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}"
TELEGRAM_MSG_FROM_ID: str = os.getenv("TELEGRAM_MSG_FROM_ID", "")
