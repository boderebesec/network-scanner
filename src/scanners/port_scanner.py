import socket
import struct
from scapy.all import sr1, send, IP, TCP

class AdvancedPortScanner:
    def __init__(self, target_host):
        """
        Initialize the AdvancedPortScanner with the target host.
        
        :param target_host: The target host to scan.
        """
        self.target_host = target_host
        self.open_ports = []
        self.scan_type = 'TCP'

    def set_scan_type(self, scan_type):
        """
        Set the scan type.
        
        :param scan_type: The scan type (TCP, SYN, FIN, XMAS).
        """
        self.scan_type = scan_type

    def stealth_scan(self, port):
        """
        Perform a stealth scan on the specified port.
        
        :param port: The port to scan.
        :return: True if the port is open, False otherwise.
        """
        if self.scan_type == 'SYN':
            ans = sr1(IP(dst=self.target_host)/TCP(dport=port,flags="S"), timeout=2)
            if ans and ans.haslayer(TCP) and ans[TCP].flags == 0x12:
                send(IP(dst=self.target_host)/TCP(dport=port,flags="R"))
                return True
        return False

    def scan_port(self, port):
        """
        Scan a single port.
        
        :param port: The port to scan.
        :return: True if the port is open, False otherwise.
        """
        if self.scan_type != 'TCP':
            return self.stealth_scan(port)
            
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        try:
            result = sock.connect_ex((self.target_host, port))
            if result == 0:
                self.open_ports.append(port)
            sock.close()
            return result == 0
        except:
            return False

    def scan_range(self, start_port, end_port):
        """
        Scan a range of ports.
        
        :param start_port: The starting port of the range.
        :param end_port: The ending port of the range.
        :return: A list of open ports.
        """
        for port in range(start_port, end_port + 1):
            self.scan_port(port)
        return self.open_ports