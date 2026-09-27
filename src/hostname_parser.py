import argparse
import socket
# couldn't implement in main so here it goes

RED = '\033[91m'
BOLD = '\033[1m'
END = '\033[0m'


def parse_hostname():
    try:
        parser = argparse.ArgumentParser(
            description="give hostname to translate: ", usage=f"{RED}python hostname_parser.py --hostname [HOSTNAME]{END}")
        parser.add_argument("--hostname", action="store",
                            dest="hostname", required=True)
        args = parser.parse_args()
        host = args.hostname
        ip_addr = socket.gethostbyname(args.hostname)
        print(host, "->", ip_addr)
    except socket.gaierror as e:
        print(f"Error: could not resolve '{args.hostname}': {e}")
    except KeyboardInterrupt:
        print("KeyboardInterruption")
    except Exception as e:
        print("Error: ", e)


if __name__ == "__main__":
    parse_hostname()
