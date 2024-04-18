import os
import time

def check_system_uptime(min_uptime_seconds):
    """ Returns True if the system uptime is above the minimum, false otherwise. """
    with open('/proc/uptime', 'r') as f:
        uptime_seconds = float(f.readline().split()[0])
        return uptime_seconds > min_uptime_seconds

# Example usage:
# check_system_uptime(86400)  # System should be up for more than 1 day
