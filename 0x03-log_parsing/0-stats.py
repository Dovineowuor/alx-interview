#!/usr/bin/env python3
import sys
import signal

total_file_size = 0
status_codes = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}

def print_stats():
    global total_file_size
    global status_codes

    print(f"File size: {total_file_size}")
    for status_code in sorted(status_codes.keys()):
        if status_codes[status_code] > 0:
            print(f"{status_code}: {status_codes[status_code]}")
    print("\n")
    total_file_size = 0
    status_codes = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0
    }

def handle_sigint(sig, frame):
    print_stats()
    sys.exit(0)

signal.signal(signal.SIGINT, handle_sigint)

counter = 0
for line in sys.stdin:
    if not line.strip():
        continue
    try:
        fields = line.strip().split(" ")
        ip_address = fields[0]
        date = fields[2][1:]
        request = fields[5]
        status_code = int(fields[7])
        file_size = int(fields[8])

        if status_code not in status_codes:
            continue

        total_file_size += file_size
        status_codes[status_code] += 1
        counter += 1
    except Exception:
        continue

    if counter == 10:
        print_stats()
        counter = 0
