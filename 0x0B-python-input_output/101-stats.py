#!/usr/bin/python3
'''Module to lookup for the method'''

import signal

#Define a signal handler to handle keyboard interruption (CTRL + C)
def signal_handler(sig, frame):
    print_statistics()

# Initialize variables to store statistics
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

# Function to print the statistics
def print_statistics():
    print(f"Total file size: {total_file_size}")
    for status_code in sorted(status_code_count.keys()):
        if status_code_count[status_code] > 0:
            print(f"{status_code}: {status_code_count[status_code]}")

# Register the signal handler for keyboard interruption
signal.signal(signal.SIGINT, signal_handler)

# Main loop to read and process input
try:
    line_count = 0
    while True:
        input_line = input("Enter the input line: ")
        parts = input_line.split()
        file_size = int(parts[-1])
        total_file_size += file_size
        status_code = int(parts[-2])
        if status_code in status_code_count:
            status_code_count[status_code] += 1
        line_count += 1
        if line_count % 10 == 0:
            print_statistics()
except KeyboardInterrupt:
    print_statistics()

