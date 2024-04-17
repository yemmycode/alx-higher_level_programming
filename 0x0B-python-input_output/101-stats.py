#!/usr/bin/python3

import sys
import signal

status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
total_size = 0
line_count = 0

def print_metrics():
    """Function to print the metrics."""
    print("Total file size: File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code]:
            print("{}: {}".format(code, status_codes[code]))

def signal_handler(sig, frame):
    """Signal handler for keyboard interruption."""
    print_metrics()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line_count += 1
        data = line.split()
        try:
            status_code = int(data[-2])
            file_size = int(data[-1])
            total_size += file_size
            if status_code in status_codes:
                status_codes[status_code] += 1
        except (IndexError, ValueError):
            pass  

        if line_count % 10 == 0:
            print_metrics()

except KeyboardInterrupt:
    print_metrics()
