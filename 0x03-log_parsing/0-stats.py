import sys
import signal

def signal_handler(signal, frame):
    print("File size: ", total_size)
    for status, count in sorted(status_codes.items()):
        if count > 0:
            print("{}: {}".format(status, count))
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
lines_processed = 0

for line in sys.stdin:
    lines_processed += 1
    elements = line.split()
    try:
        status = int(elements[-2])
        size = int(elements[-1])
    except (ValueError, IndexError):
        continue

    if status in status_codes:
        status_codes[status] += 1
        total_size += size

    if lines_processed % 10 == 0:
        print("File size: ", total_size)
        for status, count in sorted(status_codes.items()):
            if count > 0:
                print("{}: {}".format(status, count))

