"""EVN power outage schedule checker service."""

# cSpell:disable
from datetime import datetime, timedelta

import requests
from bs4 import BeautifulSoup

from src.config import constants

DATE_FORMAT = "%d-%m-%Y"
SCHEDULE_LOOKAHEAD_DAYS = 30


def check_ma_khach_hang(ma_kh: str, ten_kh: str):
    """Check the power outage schedule for a customer by their customer code.

    Args:
        ma_kh: Customer code (mã khách hàng).
        ten_kh: Customer name (tên khách hàng).

    Returns:
        A tuple of (header_text, schedule_items) on success, or None on failure.
    """
    try:
        date_from = datetime.now().strftime(DATE_FORMAT)
        date_to = (datetime.now() + timedelta(days=SCHEDULE_LOOKAHEAD_DAYS)).strftime(
            DATE_FORMAT
        )
        url = (
            f"{constants.URL_CHECK_CUP_DIEN}"
            f"?tuNgay={date_from}"
            f"&denNgay={date_to}"
            f"&maKH={ma_kh}"
            f"&ChucNang=MaKhachHang"
        )

        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        texts_info = soup.find_all("p", class_="info")
        text_no = "LỊCH CÚP ĐIỆN: " + ten_kh

        return text_no, texts_info
    except (requests.RequestException, AttributeError):
        return None
