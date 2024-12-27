# Advanced Network Scanner

A comprehensive network scanning and security assessment tool built in Python. This tool provides both basic and advanced network scanning capabilities with a focus on security analysis and network mapping.

## Features

## Basic Scanning:

• TCP/UDP port scanning

• Service version detection

• Basic vulnerability checks

• Network host discovery

## Advanced Features:

• OS fingerprinting

• Stealth scanning (SYN, FIN, XMAS)

• Custom payload injection

• Banner grabbing

• Network topology mapping

• SSL/TLS analysis

## Installation

```bash
# Clone the repository
git clone https://github.com/boderebesec/network-scanner.git

# Navigate to directory
cd network-scanner

# Create virtual environment
python -m venv venv

# Activate virtual environment
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Install requirements
pip install -r requirements.txt
```

## Usage

```bash
# Basic port scan
python main.py example.com -p 1-100

# Advanced scan with OS detection
python main.py example.com -p 1-1000 --os-detect

# Stealth SYN scan with SSL analysis
python main.py example.com -p 1-443 -s SYN --ssl-analyze
```

## Project Structure

```bash
network_scanner/
├── src/
│   ├── scanners/          # Basic scanning modules
│   ├── advanced/          # Advanced scanning features
│   └── utils/             # Utility functions
├── tests/                 # Test suites
├── requirements.txt       # Project dependencies
└── main.py               # Main execution file
```

## Requirements

```bash
• Python 3.8+
• scapy>=2.4.5
• cryptography>=3.4.7
• python-nmap>=0.7.1
• requests>=2.26.0
```

## Security Notice

This tool is intended for authorized security testing only. Unauthorized scanning of networks or systems may be illegal. Always obtain proper permissions before conducting any security assessments.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

Junior Boderebe

• GitHub: @boderebesec
