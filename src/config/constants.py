import ast
import os

import dotenv

dotenv.load_dotenv()
#
LIST_MA_KH = ast.literal_eval(os.getenv('LIST_MA_KH'))
DELAY_IN_SECONDS = 86400
#
URL_CHECK_CUP_DIEN = os.getenv('URL_CHECK_CUP_DIEN')
PAGE_ACCESS_TOKEN = os.getenv('PAGE_ACCESS_TOKEN')
RECIPIENT_ID = os.getenv('RECIPIENT_ID')
