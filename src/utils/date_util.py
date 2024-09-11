from datetime import datetime, date
import re


def extract_dates_from_text(text):
    # Define a regular expression pattern for matching dates in the format "dd/mm/yyyy"
    date_pattern = re.compile(r'\b\d{2}/\d{2}/\d{4}\b')

    # Find all matches in the input text
    matches = date_pattern.findall(text)

    return matches


def compare_with_today(target_date_str):
    # Convert target date string to a datetime object
    target_date = datetime.strptime(target_date_str, '%d/%m/%Y').date()

    # Get today's date
    today_date = date.today()

    # Compare the target date with today's date
    if target_date >= today_date:
        return True
    return False
