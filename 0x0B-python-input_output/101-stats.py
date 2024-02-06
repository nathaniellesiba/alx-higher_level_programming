#!/usr/bin/python3
'''Module to lookup for the method'''

import sys

def compute_metrics():
    total_size = 0
    status_codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            ip, _, _, status_code, file_size = line.split(' ')[0], line.split(' ')[-2], line.split(' ')[-1]
            total_size += int(file_size)
            status_codes[status_code] += 1

            if line_count % 10 == 0:
                print(f"Total file size: {total_size}")
                for code in sorted(status_codes.keys()):
                    if status_codes[code] > 0:
                        print(f"{code}: {status_codes[code]}")

    except KeyboardInterrupt:
        print(f"Total file size: {total_size}")
        for code in sorted(status_codes.keys()):
            if status_codes[code] > 0:
                print(f"{code}: {status_codes[code]}")

compute_metrics()
