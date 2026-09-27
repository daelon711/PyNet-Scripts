import ddos_attack
import mac_spoofing
import password_generator
import web_scraping
import port_scanner
import keylogger
import check_file_type
import service_comparator
import paramiko_study
import glob_to_re
import endpoint_scan
import email_utils
import json_http
import image_read
import sys


RED = '\033[91m'
BOLD = '\033[1m'
END = '\033[0m'
GREEN = '\033[1;32;40m'

# existing tools


def check_length():
    if len(sys.argv) < 2 or len(sys.argv) > 2:
        print(f"\n{RED}--------> {END}")
        print(f"{RED}Usage: python main.py <tool_number>{END}")
        print("Available tools:"
              " 1: DDoS\n"
              " 2: Password Generator\n"
              " 3: MAC Spoofing (Linux only)\n"
              " 4: Web Scraping\n"
              " 5: Port Scanner\n"
              " 6: Keylogger\n"
              " 7: Check File Type\n"
              " 8: Service Comparator\n"
              " 9: Paramiko SSH Command Execution\n"
              " 10: Glob to regex conversion\n"
              " 11: Endpoint scanner\n"
              " 12: Email validator/maker\n"
              " 13: Json dumper\n"
              " 14: Image Reader\n"
              )
        print(
            f"{GREEN}[!] Invalid number of arguments \n[!] look above for preference{END}")
    # colors are cool

        sys.exit(1)


def main():

    check_length()

    user_preference = sys.argv[1]

    try:
        match user_preference:
            case '1':
                ddos_attack.start_attack()
            case '2':
                password_generator.generate_random_password()
            case '3':
                mac_spoofing.spoof()
            case '4':
                web_scraping.grab_web()
            case '5':
                port_scanner.scan()
            case '6':
                keylogger.log_keys()
            case '7':
                check_file_type.check_type()
            case '8':
                service_comparator.compare()
            case '9':
                paramiko_study.connection()
            case '10':
                glob_to_re.glob_to_regex()
            case '11':
                endpoint_scan.path_scan()
            case '12':
                email_utils.interactive_email_builder()
            case '13':
                json_http.fetch_api_data()
            case '14':
                image_read.read_image()
            case _:
                print("INVALID, choose a number from the options")

    except Exception as e:
        print(f"\n[!] error while running the tool: {e}\n")
        return
    except KeyboardInterrupt:
        print("\n[!] Keyboard interrupt, exiting...")
        return


if __name__ == "__main__":
    main()
