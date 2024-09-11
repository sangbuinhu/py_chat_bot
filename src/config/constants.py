import ast
import os

import dotenv

dotenv.load_dotenv()
#
LIST_MA_KH = ast.literal_eval(os.getenv('LIST_MA_KH'))
DELAY_IN_SECONDS = 86400
#
URL_CHECK_CUP_DIEN = os.getenv('URL_CHECK_CUP_DIEN')

# Telegram
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_CHAT_BOT_TOKEN')
TELEGRAM_BOT_BASE_URL = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}"
TELEGRAM_MSG_FROM_ID = os.getenv('TELEGRAM_MSG_FROM_ID')
