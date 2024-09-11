from datetime import datetime, timedelta

import requests
from bs4 import BeautifulSoup

from src.config import constants


def check_ma_khach_hang(ma_kh, ten_kh):
    try:
        date_from = datetime.now().strftime('%d-%m-%Y')
        # date_from = "25-01-2023"
        date_to = (datetime.now() + timedelta(days=30)).strftime('%d-%m-%Y')
        url = f"{constants.URL_CHECK_CUP_DIEN}" \
              f"?tuNgay={date_from}" \
              f"&denNgay={date_to}" \
              f"&maKH={ma_kh}" \
              f"&ChucNang=MaKhachHang"

        response = requests.request("GET", url)
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        texts_info = soup.findAll('p', class_='info')
        text_no = "LỊCH CÚP ĐIỆN: " + ten_kh

        # print(texts_info, text_no)
        return text_no, texts_info
    except Exception:
        return None
