def check_logs_for_errors(log_file, error_patterns):
    """ Returns True if no errors are found in the log file, false otherwise. """
    with open(log_file) as file:
        for line in file:
            for pattern in error_patterns:
                if pattern in line:
                    return False
    return True

# Example usage:
# check_logs_for_errors('/var/log/syslog', ['error', 'failed'])
