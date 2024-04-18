import subprocess

def check_service_running(service_name):
    """ Returns True if the service is running, false otherwise. """
    status = subprocess.run(['systemctl', 'status', service_name], capture_output=True)
    return 'active (running)' in str(status.stdout)

# Example usage:
# check_service_running('apache2')  # Check if Apache2 is running
