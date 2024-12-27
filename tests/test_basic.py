import unittest
from src.scanners.port_scanner import AdvancedPortScanner
from src.scanners.service_detector import ServiceDetector
from src.scanners.vulnerability_scanner import VulnerabilityScanner

class TestBasicFeatures(unittest.TestCase):

    def setUp(self):
        self.target_host = "example.com"
        self.port_scanner = AdvancedPortScanner(self.target_host)
        self.service_detector = ServiceDetector(self.target_host)
        self.vulnerability_scanner = VulnerabilityScanner(self.target_host)

    def test_port_scanner_tcp(self):
        """Test TCP port scanning"""
        self.port_scanner.set_scan_type('TCP')
        open_ports = self.port_scanner.scan_range(80, 81)
        self.assertIsInstance(open_ports, list)

    def test_service_detection(self):
        """Test service detection on common ports"""
        common_ports = [80, 443]
        services = self.service_detector.detect_services(common_ports)
        self.assertIsInstance(services, dict)
        for port in common_ports:
            self.assertIn(port, services)

    def test_vulnerability_scanner(self):
        """Test vulnerability scanning"""
        vulnerabilities = self.vulnerability_scanner.scan()
        self.assertIsInstance(vulnerabilities, list)

if __name__ == "__main__":
    unittest.main()