import sys
from pathlib import Path
import utils

def display_log_counts(log_dict: dict):
    """
    Prints a summary of log levels and their counts in a tabular format.

    Args:
        log_dict (dict): A dictionary containing log levels as keys and count as values.
    """
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, entries in log_dict.items():
        print(f"{level:<16} | {entries:<8}")

def display_detailed_level(log_dict: list, detailed_level: str):
    """
    Prints detailed info by level.

    Args:
        log_dict (list): List of parsed log.
        detailed_level (string): Wich level must be shoq in details.
    """
    filtered = list(utils.filter_logs_by_level(log_dict, detailed_level))#!!!! поміняти на списковий віраз
    if len(filtered)== 0:
        return None
    print('')
    print(f'Деталі логів для рівня \'{detailed_level.upper()}\':')
    for row in filtered:
        print(row["timestamp"] +' - '+  row["message"])
        

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: python {sys.argv[0]} /path/tо/logfile.log")
        print(f"or python {sys.argv[0]} /path/tо/logfile.log <level>")
    else:
        directory_path = sys.argv[1]
        log_dict = utils.load_logs(directory_path)
        count_by_level = utils.count_logs_by_level(log_dict)
        display_log_counts(count_by_level)
        if len(sys.argv) == 3:
            display_detailed_level(log_dict, sys.argv[2])