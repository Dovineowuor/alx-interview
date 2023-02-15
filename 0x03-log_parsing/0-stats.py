#!/usr/bin/env python3
import sys

status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
total_size = 0
counter = 0

try:
    for line in sys.stdin:
        elements = line.split()
        if len(elements) != 9:
            continue

        try:
            size = int(elements[-1])
            code = int(elements[-2])
        except ValueError:
            continue

        if code not in status_codes:
            continue

        total_size += size
        status_codes[code] += 1
        counter += 1

        if counter == 10:
            print("File size: {}".format(total_size))
            for code in sorted(status_codes.keys()):
                if status_codes[code] != 0:
                    print("{}: {}".format(code, status_codes[code]))
            counter = 0
except KeyboardInterrupt:
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] != 0:
            print("{}: {}".format(code, status_codes[code]))
    sys.exit()
