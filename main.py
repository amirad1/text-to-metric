from prometheus_client import start_http_server, Counter
from dotenv import load_dotenv
import time, os
from collections import defaultdict

load_dotenv()

file_name = os.getenv('FILE_PATH', "a.txt")
metric_name = os.getenv('METRIC_NAME', "text_total")
interval = os.getenv('INTERVAL', 2)
port = 9098

line_counts = defaultdict(int)
previous_lines = []

metric = Counter(metric_name, "Your text to metric")

def log_collect():   
    global line_counts, previous_lines

    with open(file_name) as file:
        current_lines = file.read().splitlines()

    current_line_count = len(current_lines)
    
    if current_line_count < len(previous_lines):
        line_counts.clear()
        previous_lines = current_lines.copy()
        return
    
    # Find new lines since last check
    new_lines = current_lines[len(previous_lines):]
    
    # Update counts for each new line
    for line in new_lines:
        line_counts[line] += 1
        # Increment the metric for this specific context
        metric.labels(line).inc(1)
    
    # Update previous lines for next comparison
    previous_lines = current_lines.copy()

if __name__ == "__main__":
    start_http_server(port)
    print("Exporter started at http://localhost:", port)
    while True:
        log_collect() 
        time.sleep(interval)