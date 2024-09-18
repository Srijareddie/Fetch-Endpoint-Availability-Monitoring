**Endpoint Availability Monitoring Script**

**Overview:**
This script checks the availability of endpoints (URLs) listed in a YAML config file. It sends HTTP requests to each endpoint, tracks if they’re “up” based on the response time and status codes, and shows the availability percentage for each domain. The script runs continuously, checking every 15 seconds.

**Features:**
Supports GET and other HTTP methods.
Lets you configure headers and request bodies for each endpoint.
Marks an endpoint as “up” if:
The status code is in the 2xx range.
The response time is under 500ms.
Displays the availability percentage for each domain after every cycle.
Runs in an infinite loop with a 15-second delay between checks.

**How to Use????**
Create a YAML config file listing the endpoints, methods, headers, and request bodies (if needed).
Run the script by passing the path to the config file:
bash
Copy code
python script.py <config_file_path>
That’s it! The script will keep checking the endpoints and show availability stats after each cycle.
