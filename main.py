import argparse
from src.scanners.port_scanner import AdvancedPortScanner
from src.advanced.os_detector import OSDetector
from src.advanced.ssl_analyzer import SSLAnalyzer

def main():
    """
    Main function to run the Advanced Network Scanner.
    """
    parser = argparse.ArgumentParser(description='Advanced Network Scanner')
    parser.add_argument('target', help='Target host to scan')
    parser.add_argument('-p', '--ports', help='Port range (e.g., 1-100)', default='1-1000')
    parser.add_argument('-s', '--scan-type', help='Scan type (TCP/SYN/FIN)', default='TCP')
    parser.add_argument('--os-detect', action='store_true', help='Enable OS detection')
    parser.add_argument('--ssl-analyze', action='store_true', help='Analyze SSL/TLS')
    args = parser.parse_args()

    scanner = AdvancedPortScanner(args.target)
    scanner.set_scan_type(args.scan_type)

    if args.os_detect:
        os_detector = OSDetector(args.target)
        print(f"OS Detection: {os_detector.get_ttl_guess()}")

    if args.ssl_analyze:
        ssl_analyzer = SSLAnalyzer(args.target)
        print("SSL/TLS Analysis:", ssl_analyzer.analyze_ssl())

    start_port, end_port = map(int, args.ports.split('-'))
    open_ports = scanner.scan_range(start_port, end_port)
    
    print(f"\nOpen ports on {args.target}:")
    for port in open_ports:
        print(f"Port {port} is open")

if __name__ == "__main__":
    main()