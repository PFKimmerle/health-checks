import psutil

def check_memory_usage(max_percent):
    """ Returns True if memory usage is within limits, false otherwise. """
    memory = psutil.virtual_memory()
    return memory.percent < max_percent

# Example usage:
# check_memory_usage(80)  # Ensure memory usage is below 80%
