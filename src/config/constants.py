"""Application constants loaded from environment variables."""

import ast
import os

from dotenv import load_dotenv

load_dotenv()

LIST_MA_KH: dict = ast.literal_eval(os.getenv("LIST_MA_KH", "{}"))
DELAY_IN_SECONDS: int = 86400

URL_CHECK_CUP_DIEN: str = os.getenv("URL_CHECK_CUP_DIEN", "")

# VNAppMob API
URL_VN_APP_MOB_API_KEY: str = "https://api.vnappmob.com/api/request_api_key?scope=gold"
URL_VN_APP_MOB_GOLD_PRICE: str = "https://vapi.vnappmob.com/api/v2/gold/sjc"

# Telegram
TELEGRAM_TOKEN_POWER_OUTAGE: str = os.getenv("TELEGRAM_TOKEN_POWER_OUTAGE", "")
TELEGRAM_TOKEN_MARKET_PULSE: str = os.getenv("TELEGRAM_TOKEN_MARKET_PULSE", "")

TELEGRAM_BOT_BASE_URL: str = "https://api.telegram.org/bot"

TELEGRAM_MSG_FROM_ID: str = os.getenv("TELEGRAM_MSG_FROM_ID", "")
TELEGRAM_CHAT_ID_MARKET_PULSE: str = os.getenv("TELEGRAM_CHAT_ID_MARKET_PULSE", "")

# TwelveData API
TWELVEDATA_API_KEY: str = os.getenv("TWELVEDATA_API_KEY", "")
URL_TWELVEDATA_PRICE: str = "https://api.twelvedata.com/price"
