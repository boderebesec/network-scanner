from scapy.all import IP, ICMP, TCP, sr1

class OSDetector:
    def __init__(self, target_host):
        self.target_host = target_host

    def get_ttl_guess(self):
        """Guess OS based on TTL"""
        try:
            ans = sr1(IP(dst=self.target_host)/ICMP(), timeout=2)
            if ans:
                ttl = ans.ttl
                if ttl <= 64:
                    return "Linux/Unix"
                elif ttl <= 128:
                    return "Windows"
                else:
                    return "Cisco/Network Device"
        except:
            return "Unknown"

    def tcp_fingerprint(self):
        """Advanced TCP/IP stack fingerprinting"""
        try:
            ans = sr1(IP(dst=self.target_host)/TCP(dport=80,flags="S"))
            if ans:
                window = ans[TCP].window
                options = ans[TCP].options
                # Analyze TCP options and window size for OS hints
                return self.analyze_tcp_signature(window, options)
        except:
            return "Unknown"