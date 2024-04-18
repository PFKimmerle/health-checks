import psutil

def check_temperature(max_temp):
    """ Returns True if the temperature is within safe limits, false otherwise. """
    temps = psutil.sensors_temperatures()
    if 'coretemp' in temps:
        for entry in temps['coretemp']:
            if entry.current > max_temp:
                return False
    return True

# Example usage:
# check_temperature(70)  # CPU temperature should not exceed 70 degrees Celsius
