import random
import time

status_codes = [200, 301, 400, 401, 403, 404, 405, 500]

def generate_log_line():
    ip_address = ".".join(str(random.randint(0, 255)) for i in range(4))
    date = time.strftime("%d/%b/%Y:%H:%M:%S +0000", time.gmtime())
    method = "GET"
    endpoint = "/projects/260"
    http_version = "HTTP/1.1"
    status_code = str(random.choice(status_codes))
    file_size = str(random.randint(0, 10000))
    log_line = f"{ip_address} - [{date}] \"{method} {endpoint} {http_version}\" {status_code} {file_size}"
    return log_line

while True:
    print(generate_log_line())
    time.sleep(0.5)