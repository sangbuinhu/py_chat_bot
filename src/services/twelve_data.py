# cSpell:disable
"""TwelveData API service for fetching exchange rates and commodity prices."""

import requests

from src.config import constants
from src.utils import log_util

_SYMBOLS = "USD/VND,XAU/USD,JPY/USD"


def get_prices_world() -> str | None:
    """Fetch and format exchange rates/gold price for Telegram. Returns message string or None on failure."""
    try:
        response = requests.get(
            constants.URL_TWELVEDATA_PRICE,
            params={
                "symbol": _SYMBOLS,
                "apikey": constants.TWELVEDATA_API_KEY,
            },
            timeout=10,
        )
        response.raise_for_status()
        data = response.json()

        usd_vnd = float(data["USD/VND"]["price"])
        xau_usd = float(data["XAU/USD"]["price"])
        jpy_usd = float(data["JPY/USD"]["price"])

        xau_vnd = xau_usd * usd_vnd
        jpy_vnd = jpy_usd * usd_vnd

        def fmt(value: float) -> str:
            return f"{value:,.0f}"

        response = (
            f"{'--' * 30}\n"
            f"TỶ GIÁ & GIÁ VÀNG THẾ GIỚI\n"
            f"{'--' * 30}\n"
            f"{'USD/VND:':<12} {fmt(usd_vnd):>20} VND\n"
            f"{'JPY/VND:':<12} {fmt(jpy_vnd):>23} VND\n"
            f"{'XAU/USD:':<12} {fmt(xau_usd):>22} USD\n"
            f"{'XAU/VND:':<12} {fmt(xau_vnd):>15} VND\n"
        )

        print(response)

        return response
    except (requests.RequestException, ValueError, KeyError) as e:
        log_util.show_log(e)
        return None
