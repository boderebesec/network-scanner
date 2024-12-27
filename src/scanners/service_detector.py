import socket

class ServiceDetector:
    def __init__(self, target_host):
        self.target_host = target_host

    def detect_service(self, port):
        """Detect service running on a given port by grabbing the banner"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            sock.connect((self.target_host, port))
            sock.send(b'HEAD / HTTP/1.1\r\n\r\n')
            banner = sock.recv(1024).decode().strip()
            sock.close()
            return banner
        except Exception as e:
            return str(e)

    def detect_services(self, ports):
        """Detect services running on a list of ports"""
        services = {}
        for port in ports:
            banner = self.detect_service(port)
            services[port] = banner
        return services

# Example usage
if __name__ == "__main__":
    detector = ServiceDetector("example.com")
    common_ports = [80, 443, 22, 21, 25]
    services = detector.detect_services(common_ports)
    for port, service in services.items():
        print(f"Port {port}: {service}")