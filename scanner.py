# -------------------------------------------------------------
# Project: Python-Network-Scanner
# Author: Krystel E Albertson
# Business: Lock it Down Solutions
# Date: February 2026
# -------------------------------------------------------------

import socket
from datetime import datetime

# Simple Port Scanner
target = input("Enter the IP address to scan: ")
print("-" * 50)
print(f"Scanning Target: {target}")
print(f"Scanning started at: {str(datetime.now())}")
print("-" * 50)

try:
    # Scan ports 1 through 1024
    for port in range(1, 1025):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        
        # Returns 0 if port is open
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is OPEN")
        s.close()

except Exception as e:
    print(f"\n Error: {e}")
