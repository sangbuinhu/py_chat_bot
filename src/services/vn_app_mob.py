# cSpell:disable
"""VnAppMob API service."""

from datetime import datetime

import requests

from src.config import constants
from src.utils import log_util


def request_api_key() -> str | None:
    """Request a gold-scope API key from vnappmob. Returns the token string or None on failure."""
    try:
        response = requests.get(constants.URL_VN_APP_MOB_API_KEY, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data.get("results") or None
    except (requests.RequestException, ValueError):
        return None


def get_price_gold() -> str | None:
    """Get the current gold price using the API key.
    Returns formatted price message or None on failure."""

    api_key = request_api_key()
    if not api_key:
        return None

    try:
        response = requests.get(
            constants.URL_VN_APP_MOB_GOLD_PRICE,
            headers={"Authorization": f"Bearer {api_key}"},
            timeout=10,
        )
        response.raise_for_status()
        data = response.json()
        results = data.get("results", [])
        if not results:
            return None

        item = results[0]
        updated_at = datetime.fromtimestamp(int(item["datetime"])).strftime(
            "%d/%m/%Y %I:%M %p"
        )

        def fmt(value: str) -> str:
            return f"{float(value):,.0f}"

        response = (
            f"{'--' * 30}\n"
            f"VÀNG SJC ({updated_at})\n"
            f"Đơn vị tính: VNĐ / lượng\n"
            f"{'--' * 30}\n"
            f"{'Loại':<10} {'Mua':>3} {'Bán':>20}\n"
            f"{'--' * 30}\n"
            f"{'1C:':<10} {fmt(item['buy_1c']):>8} {fmt(item['sell_1c']):>14}\n"
        )

        return response
    except (requests.RequestException, ValueError, KeyError) as e:
        log_util.show_log(e)
        return None
