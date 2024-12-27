import ssl
import socket
from cryptography import x509

class SSLAnalyzer:
    def __init__(self, target_host, port=443):
        """
        Initialize the SSLAnalyzer with the target host and port.
        
        :param target_host: The target host to analyze SSL/TLS.
        :param port: The port to analyze SSL/TLS (default is 443).
        """
        self.target_host = target_host
        self.port = port

    def analyze_ssl(self):
        """
        Analyze the SSL/TLS configuration of the target host.
        
        :return: A dictionary with SSL/TLS analysis results.
        """
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE

        try:
            with socket.create_connection((self.target_host, self.port)) as sock:
                with context.wrap_socket(sock, server_hostname=self.target_host) as ssock:
                    cert = ssock.getpeercert(binary_form=True)
                    cert_obj = x509.load_der_x509_certificate(cert)
                    
                    return {
                        'version': ssock.version(),
                        'cipher': ssock.cipher(),
                        'cert_expires': cert_obj.not_valid_after,
                        'cert_issuer': cert_obj.issuer
                    }
        except Exception as e:
            return f"SSL Analysis failed: {str(e)}"