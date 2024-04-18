import psutil

def check_cpu_usage(max_percent):
    """ Returns True if cpu usage is within limits, false otherwise. """
    usage = psutil.cpu_percent(1)
    return usage < max_percent

# Example usage:
# check_cpu_usage(75)  # Ensure CPU usage is below 75%
