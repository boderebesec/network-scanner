import ipaddress
import socket

def is_valid_ip(ip):
    """Check if the given string is a valid IP address."""
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def is_valid_port(port):
    """Check if the given number is a valid port."""
    return 0 <= port <= 65535

def get_ip_range(start_ip, end_ip):
    """Generate a list of IP addresses in the given range."""
    try:
        start = ipaddress.ip_address(start_ip)
        end = ipaddress.ip_address(end_ip)
        return [str(ip) for ip in ipaddress.summarize_address_range(start, end)]
    except ValueError:
        return []

def get_open_ports(target_host, ports):
    """Check for open ports on the target host."""
    open_ports = []
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target_host, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

# Example usage
if __name__ == "__main__":
    print(is_valid_ip("192.168.1.1"))  # True
    print(is_valid_ip("999.999.999.999"))  # False
    print(is_valid_port(80))  # True
    print(is_valid_port(70000))  # False
    print(get_ip_range("192.168.1.1", "192.168.1.5"))
    # ['192.168.1.1', '192.168.1.2', '192.168.1.3', '192.168.1.4', '192.168.1.5']