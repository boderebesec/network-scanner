from scapy.all import IP, TCP, sr1

class StealthScanner:
    def __init__(self, target_host):
        self.target_host = target_host

    def syn_scan(self, port):
        """Perform a SYN scan on the specified port"""
        try:
            pkt = IP(dst=self.target_host)/TCP(dport=port, flags="S")
            response = sr1(pkt, timeout=2, verbose=0)
            if response is None:
                return "Filtered"
            elif response.haslayer(TCP):
                if response.getlayer(TCP).flags == 0x12:  # SYN-ACK
                    return "Open"
                elif response.getlayer(TCP).flags == 0x14:  # RST-ACK
                    return "Closed"
            return "Filtered"
        except Exception as e:
            return str(e)

    def scan_ports(self, ports):
        """Scan a list of ports using SYN scan"""
        results = {}
        for port in ports:
            result = self.syn_scan(port)
            results[port] = result
        return results

# Example usage
if __name__ == "__main__":
    scanner = StealthScanner("example.com")
    common_ports = [80, 443, 22, 21, 25]
    results = scanner.scan_ports(common_ports)
    for port, status in results.items():
        print(f"Port {port}: {status}")