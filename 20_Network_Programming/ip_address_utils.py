# ip_address_utils.py

"""
Definition: An IP address is a unique string of characters that identifies each computer using the Internet Protocol to communicate over a network.
"""

import socket

def get_ip_info():
    hostname = "localhost"
    try:
        ip_address = socket.gethostbyname(hostname)
        print(f"Hostname: {hostname}")
        print(f"IP Address: {ip_address}")
    except Exception as e:
        print(f"Error: {e}")

get_ip_info()
