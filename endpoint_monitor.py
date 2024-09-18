import yaml
import requests
import time
from collections import defaultdict
import sys
from urllib.parse import urlparse
# Function to parse the configuration YAML file
def parse_config(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)
# Function to extract the domain from a given URL
def get_domain(url):
    return urlparse(url).netloc
# Function to send HTTP requests to the given endpoint and track availability

def send_request(endpoint):
    url = endpoint['url']
    method = endpoint.get('method', 'GET')
    headers = endpoint.get('headers', {})
    body = endpoint.get('body')
    
    try:
        start_time = time.time()
        response = requests.request(method, url, headers=headers, data=body, timeout=0.5)
        elapsed_time = (time.time() - start_time) * 1000  # Convert to milliseconds
        
        is_up = 200 <= response.status_code < 300 and elapsed_time < 500
        print(f"Debug: {url} - Status: {response.status_code}, Time: {elapsed_time:.2f}ms, Up: {is_up}")
        return is_up
    except requests.RequestException as e:
        print(f"Debug: {url} - Exception: {str(e)}")
        return False
# Main function to manage the monitoring loop
def main(config_file):
    endpoints = parse_config(config_file)
    domain_stats = defaultdict(lambda: {'up': 0, 'total': 0})
    cycle_count = 0
# Infinite loop to continuously check endpoints
    while True:
        cycle_count += 1
        print(f"\nStarting cycle {cycle_count}")
        for endpoint in endpoints:
            domain = get_domain(endpoint['url'])
            is_up = send_request(endpoint)
            domain_stats[domain]['total'] += 1
            if is_up:
                domain_stats[domain]['up'] += 1

        print("\nCycle results:")
        for domain, stats in domain_stats.items():
            availability = round((stats['up'] / stats['total']) * 100)
            print(f"{domain} has {availability}% availability percentage")

        print(f"Waiting 15 seconds before next cycle...")
        time.sleep(15)
# Entry point of the script
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <config_file_path>")
        sys.exit(1)
    main(sys.argv[1])