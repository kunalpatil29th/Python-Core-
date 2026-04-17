# udp_socket_sim.py

"""
Definition: UDP (User Datagram Protocol) is a communications protocol that is primarily used for establishing low-latency and loss-tolerating connections between applications on the internet.
"""

def simulate_udp():
    print("Sending UDP Datagram to 192.168.1.1:5000...")
    message = b"Status Update"
    print(f"Packet sent: {message}")
    print("UDP is connectionless, no confirmation needed.")

simulate_udp()
