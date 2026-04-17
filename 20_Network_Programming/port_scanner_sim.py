# port_scanner_sim.py

"""
Definition: A Port Scanner is an application designed to probe a server or host for open ports. This is often used by administrators to verify security policies of their networks.
"""

def simulate_port_scan():
    target = "127.0.0.1"
    ports = [21, 22, 80, 443, 3306]
    print(f"Scanning target: {target}")
    for port in ports:
        status = "OPEN" if port in [80, 443] else "CLOSED"
        print(f"Port {port}: {status}")

simulate_port_scan()
