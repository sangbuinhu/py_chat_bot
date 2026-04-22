"""Date parsing and comparison utilities."""

from datetime import datetime, date
import re


def extract_dates_from_text(text: str) -> list[str]:
    """Extract all dates in dd/mm/yyyy format from a text string.

    Args:
        text: The input string to search for dates.

    Returns:
        A list of matched date strings in dd/mm/yyyy format.
    """
    date_pattern = re.compile(r"\b\d{2}/\d{2}/\d{4}\b")
    return date_pattern.findall(text)


def compare_with_today(target_date_str: str) -> bool:
    """Check whether a date string is today or in the future.

    Args:
        target_date_str: A date string in dd/mm/yyyy format.

    Returns:
        True if the target date is today or later, False otherwise.
    """
    target_date = datetime.strptime(target_date_str, "%d/%m/%Y").date()
    return target_date >= date.today()
