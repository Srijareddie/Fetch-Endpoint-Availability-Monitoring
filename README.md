**Endpoint Availability Monitoring Script**

**Overview:**
This program monitors the health of HTTP endpoints by checking their availability every 15 seconds. It reads a list of endpoints from a YAML file and logs the cumulative availability percentage for each domain.

**Features:**
Periodic Health Checks: Tests each endpoint every 15 seconds.
Availability Tracking:  Logs cumulative availability percentages rounded to the nearest whole number.
Detailed Logging:       Displays status codes, response times, and UP/DOWN status.
Cycle Output:           Clearly separates logs for each testing cycle.
Usage
Create a YAML Configuration File with your HTTP endpoints.
Run the Program:
bash
Copy code
node your_program.js /path/to/config.yaml

**How to Use????**
Run the script by passing the path to the config file:
python endpoint_monitor.py config.yaml

That’s it! The script will keep checking the endpoints and show availability stats after each cycle.
