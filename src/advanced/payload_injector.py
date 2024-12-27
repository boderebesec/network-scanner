import socket

class PayloadInjector:
    def __init__(self, target_host, target_port):
        self.target_host = target_host
        self.target_port = target_port

    def inject_payload(self, payload):
        """Inject a custom payload to the target host and port"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            sock.connect((self.target_host, self.target_port))
            sock.sendall(payload.encode())
            response = sock.recv(1024).decode()
            sock.close()
            return response
        except Exception as e:
            return str(e)

# Example usage
if __name__ == "__main__":
    injector = PayloadInjector("example.com", 80)
    payload = "GET / HTTP/1.1\r\nHost: example.com\r\n\r\n"
    response = injector.inject_payload(payload)
    print(response)