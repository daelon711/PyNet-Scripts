import requests
import socket
from ddos_attack import is_ip

# Check if a specific web port is open with an HTTP GET


def is_valid_domain(domain):  # checks if domain is valid

    try:
        # Attempt to resolve the domain to an IP address
        socket.gethostbyname(domain)
        return True
    except socket.gaierror:
        return False


def web_port_open(entry, port):
    if is_ip(entry) or is_valid_domain(entry):
        url = f"http://{entry}:{port}"
        try:
            response = requests.get(url, timeout=3)
            if response.status_code == 200:
                return True
        except:
            return False
    return False

# socket port scan for a list of ports


def socket_port_scan(ip, portlist):
    print(f"\n-> socket scan on {ip}\n")
    for port in portlist:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            result = sock.connect_ex((ip, port))  # creates connection
            if result == 0:  # connect 0 means open port
                print(f"Port {port} is OPEN")
            else:
                print(f"Port {port} is CLOSED")
            sock.close()
        except Exception as e:
            print(f"Error on port {port}: {e}")


def scan():
    user_entry = input(
        "Choose IP or domain(without https or / lines): ").strip()
    port = input(
        "Choose a single port (or leave blank to scan a range): ").strip()

    while not (is_ip(user_entry) or is_valid_domain(user_entry)):
        user_entry = input("Correct your IP/domain: ").strip()

    if port.isdigit():
        if web_port_open(user_entry, port):
            print(f"Port {port} on {user_entry} is OPEN (HTTP check)")
        else:
            print(f"Port {port} is CLOSED on {user_entry} (HTTP check)")
    else:
        # Default port list if no single port was given
        portlist = [20, 21, 22, 23, 25, 53, 80, 110, 143, 443, 8080]
        socket_port_scan(user_entry, portlist)


if __name__ == "__main__":
    scan()
