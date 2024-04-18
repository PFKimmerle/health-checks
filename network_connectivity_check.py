import socket

def check_network(hostname="www.google.com", port=80):
    """ Returns True if the host is reachable, false otherwise. """
    try:
        socket.create_connection((hostname, port), timeout=10)
        return True
    except OSError:
        pass
    return False

# Example usage:
# check_network()  # Check if Google is reachable
