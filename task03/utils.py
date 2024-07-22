from pathlib import Path

def input_error(func):
    """Validator on exceptions."""
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except FileNotFoundError:
            return "File is not exists."
        except TypeError:
            return "See previous error."

    return inner

def parse_log_line(line: str) -> dict:
    """
    Parses a log line and returns a dictionary with relevant information.

    Args:
        line (str): A single log line.

    Returns:
        dict: A dictionary containing parsed log information.
    """
    data, timestamp_str, log_level, message = line.strip().split(' ', 3)
    return {
        'timestamp': data + " " + timestamp_str,
        'log_level': log_level,
        'message': message.strip()
    }

@input_error
def load_logs(file_path: str):
    """
    Loads log entries from a file and returns a list of dictionaries.

    Args:
        file_path (str): Path to the log file.

    Returns:
        list: List of parsed log entries (each entry represented as a dictionary).
    """
    path = Path(file_path)
    with open(path, 'r', encoding='utf-8') as file:
        logs = [parse_log_line(line) for line in file]
    return logs

@input_error
def filter_logs_by_level(logs: list, level: str):
    """
    Filters onput list by level.

    Args:
        logs (list): List of parsed log.
        level: filter by level

    Returns:
        list: Filtered list by level.
    """
    return filter(lambda emp: emp["log_level"].upper() == level.upper(), logs)

@input_error
def count_logs_by_level(log_dict: list):
    """
    Counts of numbers by level.

    Args:
        counts (list[dict]): List of parsed log.

    Returns:
        dict: Dictionary with level and the number of cases in the file.
    """
    unique_log_levels = list({entry['log_level'] for entry in log_dict})
    res = {k: len(list(filter_logs_by_level(log_dict, k))) for k in unique_log_levels}
    return res