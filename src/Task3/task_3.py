#!/usr/bin/env python3

from collections import Counter
import sys

def parse_log_line(line: str) -> dict:
    parts = line.split(' ', 3)
    if len(parts) != 4:
        raise ValueError(f'Invalid log line: {line}')
    return {
        'timestamp': f'{parts[0]} {parts[1]}',
        'level': parts[2],
        'message': parts[3],
    }

def load_logs(file_path: str) -> list:
    logs = []
    try:
        with open(file_path, 'r') as file:
            stripped_lines = map(str.strip, file)
            non_empty_lines = filter(None, stripped_lines)

            for i, line in enumerate(non_empty_lines, 1):
                try:
                    logs.append(parse_log_line(line))
                except ValueError:
                    print(f'Line {i} error')
    except FileNotFoundError:
        print(f'File {file_path} not found')
    return logs

def filter_logs_by_level(logs: list, level: str) -> list:
    return [log for log in logs if log['level'].upper() == level.upper()]

def count_logs_by_level(logs: list) -> dict:
    levels = map(lambda log_entry: log_entry['level'], logs)
    level_counts = Counter(levels)
    result = dict(level_counts)
    return result

column_name_1 = 'Рівень логування'
column_name_2 = 'Кількість'

LEVEL_PRIORITY = {
    'DEBUG': 0,
    'INFO': 1,
    'WARNING': 2,
    'ERROR': 3
}

def display_log_counts(counts: dict):
    print(f'{column_name_1} | {column_name_2}')
    print(f'{"-" * len(column_name_1)} | {"-" * len(column_name_2)}')
    for level, count in sorted(counts.items(),
                               key = lambda item: LEVEL_PRIORITY.get(item[0], len(LEVEL_PRIORITY) + 1)):
        print(f'{level:<{len(column_name_1)}} | {count}')

def main():
    args = sys.argv
    if len(args) < 2:
        print('Enter file name')
        return

    file_path = args[1]
    level_filter = args[2] if len(args) > 2 else None

    if not (logs := load_logs(file_path)):
        print('Log file is empty')
        return

    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if level_filter:
        print(f'Деталі логів для рівня "{level_filter}":')
        for log in filter_logs_by_level(logs, level_filter):
            print(f"{log['timestamp']} - {log['message']}")

if __name__ == "__main__":
    main()