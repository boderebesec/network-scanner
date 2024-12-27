import unittest
from src.advanced.os_detector import OSDetector
from src.advanced.ssl_analyzer import SSLAnalyzer

class TestAdvancedFeatures(unittest.TestCase):

    def setUp(self):
        self.target_host = "example.com"
        self.os_detector = OSDetector(self.target_host)
        self.ssl_analyzer = SSLAnalyzer(self.target_host)

    def test_os_detection_ttl_guess(self):
        """Test OS detection based on TTL value"""
        result = self.os_detector.get_ttl_guess()
        self.assertIn(result, ["Linux/Unix", "Windows", "Cisco/Network Device", "Unknown"])

    def test_os_detection_tcp_fingerprint(self):
        """Test OS detection based on TCP fingerprinting"""
        result = self.os_detector.tcp_fingerprint()
        self.assertIn(result, ["Linux/Unix", "Windows", "Cisco/Network Device", "Unknown"])

    def test_ssl_analysis(self):
        """Test SSL/TLS analysis"""
        result = self.ssl_analyzer.analyze_ssl()
        self.assertIsInstance(result, dict)
        self.assertIn('version', result)
        self.assertIn('cipher', result)
        self.assertIn('cert_expires', result)
        self.assertIn('cert_issuer', result)

if __name__ == "__main__":
    unittest.main()