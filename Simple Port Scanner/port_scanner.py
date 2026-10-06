# Simple Port Scanner
# A beginner-friendly TCP port scanner that checks whether common
# ports on a target host are open. Use it only on hosts you own
# or are explicitly authorized to test.

import socket
import sys

# Common ports: FTP, SSH, Telnet, SMTP, DNS, HTTP, POP3, NetBIOS, IMAP,
# HTTPS, SMB, MSSQL, MySQL, RDP, PostgreSQL, Redis, HTTP-alt, RTSP, MongoDB
COMMON_PORTS = [
    21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445,
    993, 995, 1433, 1521, 3306, 3389, 5432, 6379, 8080, 8443, 27017,
]

TIMEOUT_SECONDS = 1.0


def scan_port(host: str, port: int, timeout: float) -> bool:
    """Try to open a TCP connection to host:port. Return True if open."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            return sock.connect_ex((host, port)) == 0
    except (socket.gaierror, OSError):
        return False


def parse_ports(text: str) -> list:
    """Parse a comma/range string like '80,443' or '1-100' into a port list."""
    ports = []
    for part in text.split(","):
        part = part.strip()
        if "-" in part:
            start, end = part.split("-", 1)
            ports.extend(range(int(start), int(end) + 1))
        elif part:
            ports.append(int(part))
    return ports


def main():
    if len(sys.argv) < 2:
        print("Usage: python port_scanner.py <host> [ports] [timeout]")
        print("Example: python port_scanner.py 8.8.8.8 53,443")
        print("         python port_scanner.py 192.168.1.1 1-100 0.5")
        sys.exit(1)

    host = sys.argv[1]
    ports = parse_ports(sys.argv[2]) if len(sys.argv) >= 3 else COMMON_PORTS
    timeout = float(sys.argv[3]) if len(sys.argv) >= 4 else TIMEOUT_SECONDS

    print(f"Scanning {host} for {len(ports)} port(s)...\n")
    open_ports = []
    for port in ports:
        if scan_port(host, port, timeout):
            print(f"  [OPEN]  {port}")
            open_ports.append(port)

    if open_ports:
        print(f"\nOpen ports: {open_ports}")
    else:
        print("\nNo open ports found.")


if __name__ == "__main__":
    main()
