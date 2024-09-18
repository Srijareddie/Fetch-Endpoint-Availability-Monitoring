**Endpoint Availability Monitoring Script**

**Overview:**

This program monitors the health of HTTP endpoints by checking their availability every 15 seconds. It reads a list of endpoints from a YAML file and logs the cumulative availability percentage for each domain.

**Features:**
- Periodic Health Checks: Tests each endpoint every 15 seconds.
- Availability Tracking:  Logs cumulative availability percentages rounded to the nearest whole number.
- Detailed Logging:       Displays status codes, response times, and UP/DOWN status.
- Cycle Output:           Clearly separates logs for each testing cycle.

**How to Use??**

- Run:
python endpoint_monitor.py config.yaml

**Observation:**

This script continuously monitors endpoints from a YAML file, checking their status and response time every 15 seconds. To optimize, consider increasing the request timeout, using parallel or asynchronous requests to handle multiple endpoints, and reducing logging to minimize I/O operations. For large config files, optimize parsing or use a faster format like JSON.
