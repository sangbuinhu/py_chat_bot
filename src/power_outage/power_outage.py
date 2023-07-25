import re

import requests
from datetime import datetime, timedelta

from config import constants
from bs4 import BeautifulSoup


def check_ma_khach_hang(ma_kh):
    try:
        # date_from = datetime.now().strftime('%d-%m-%Y')
        date_from = "25-01-2023"
        date_to = (datetime.now() + timedelta(days=30)).strftime('%d-%m-%Y')
        url = f"{constants.URL_CHECK_CUP_DIEN}" \
              f"?tuNgay={date_from}" \
              f"&denNgay={date_to}" \
              f"&maKH={ma_kh}" \
              f"&ChucNang=MaKhachHang"

        response = requests.request("GET", url)
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        text_no = soup.find('p', class_='ttl').get_text()
        text_info = soup.find('p', class_='info').get_text()
        text_no = re.sub(r'\s+', ' ', text_no).strip().upper()
        return text_no + ':' + text_info
    except Exception:
        return None
