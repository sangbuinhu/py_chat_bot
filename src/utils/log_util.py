import traceback

from src.utils import console


def show_log(error: Exception):
    formatted_lines = traceback.format_exc().splitlines()
    e = formatted_lines[1].strip().split(',')
    console.logger(
        file_name=(e[0] + e[1]).replace('File', '').strip(),
        function=e[-1].replace(' in', '').strip(),
        message=error.__str__()
    )
