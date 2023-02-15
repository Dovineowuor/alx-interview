# 0-stats.py
import sys
from signal import signal, SIGINT

def signal_handler(signal, frame):
    print("File size: {}".format(file_size))
    status_codes = sorted(status_codes_dict.keys())
    for code in status_codes:
        if status_codes_dict[code] > 0:
            print("{}: {}".format(code, status_codes_dict[code]))
    sys.exit(0)

signal(SIGINT, signal_handler)

file_size = 0
status_codes_dict = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}

counter = 0
for line in sys.stdin:
    items = line.split()
    if len(items) != 9:
        continue
    code = items[-2]
    if not code.isdigit():
        continue
    code = int(code)
    if code < 200 or code >= 600:
        continue
    size = int(items[-1])
    file_size += size
    status_codes_dict[str(code)] += 1
    counter += 1
    if counter % 10 == 0:
        print("File size: {}".format(file_size))
        status_codes = sorted(status_codes_dict.keys())
        for code in status_codes:
            if status_codes_dict[code] > 0:
                print("{}: {}".format(code, status_codes_dict[code]))
