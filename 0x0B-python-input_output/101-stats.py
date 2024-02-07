#!/usr/bin/python3
'''Module to lookup for the method'''


import sys

# Initialize variables to store metrics
total_file_size = 0
status_code_count = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}
line_count = 0

try:
    for line in sys.stdin:
        data = line.split()
        if len(data) > 2:
            status_code = int(data[-2])
            file_size = int(data[-1])
            total_file_size += file_size
            line_count += 1
            if status_code in status_code_count:
                status_code_count[status_code] += 1

        # Print statistics for every 10 lines
        if line_count % 10 == 0:
            print("Total file size: File size: {}".format(total_file_size))
            for code in sorted(status_code_count.keys()):
                if status_code_count[code] > 0:
                    print("{}: {}".format(code, status_code_count[code]))

except KeyboardInterrupt:
    print("Total file size: File size: {}".format(total_file_size))
    for code in sorted(status_code_count.keys()):
        if status_code_count[code] > 0:
            print("{}: {}".format(code, status_code_count[code]))

