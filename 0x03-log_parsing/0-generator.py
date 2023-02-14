import sys
import signal

def signal_handler(signal, frame):
    print("File size: ", total_file_size)
    print("Status code metrics:")
    for status_code in sorted(status_code_counts.keys()):
        print("{}: {}".format(status_code, status_code_counts[status_code]))
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

total_file_size = 0
status_code_counts = {}
line_count = 0

for line in sys.stdin:
    parts = line.strip().split()
    if len(parts) != 5:
        continue
    status_code = int(parts[4])
    if status_code not in [200, 301, 400, 401, 403, 404, 405, 500]:
        continue
    total_file_size += int(parts[5])
    line_count += 1
    if status_code in status_code_counts:
        status_code_counts[status_code] += 1
    else:
        status_code_counts[status_code] = 1
    if line_count % 10 == 0:
        print("File size: ", total_file_size)
        print("Status code metrics:")
        for status_code in sorted(status_code_counts.keys()):
            print("{}: {}".format(status_code, status_code_counts[status_code]))
