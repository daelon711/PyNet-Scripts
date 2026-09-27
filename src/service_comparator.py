import subprocess
import os


def get_services():
    # Get a list of all systemd service names
    try:
        res = subprocess.run(
            ["systemctl", "list-units", "--type=service",
                "--all", "--no-pager", "--no-legend"],
            text=True, capture_output=True, check=True
        )
        services = []
        for line in res.stdout.splitlines():
            if line.strip():
                service_name = line.split()[0]
                services.append(service_name)
        return sorted(services)
    except subprocess.CalledProcessError:
        return []


def save_services(services, filename):
    with open(filename, "w") as f:
        f.write("\n".join(services))


def load_services(filename):
    if not os.path.exists(filename):
        return []
    with open(filename, "r") as f:
        return f.read().splitlines()


def describe_service(service):
    """Get a brief description of a service using systemctl."""
    try:
        res = subprocess.run(
            ["systemctl", "status", service, "--no-pager"],
            text=True, capture_output=True, check=True
        )
        # Extract  Description line from the status output
        for line in res.stdout.splitlines():
            if "Loaded:" in line or "Active:" in line or "Description:" in line:
                print(line)
    except subprocess.CalledProcessError:
        print(f"Couldn't get status for {service}")


def compare():
    print("=== Compare ===")
    print("1. Take a snapshot of current services (first run)")
    print("2. Take another snapshot and compare (second run)")
    print("-----------------------------------------")
    first_file = input(
        "Enter the FIRST filename (e.g: baseline.txt): ").strip()
    if not os.path.exists(first_file):
        # First run: save current services
        services = get_services()
        save_services(services, first_file)
        print(
            f"saved to {first_file}. Run the script again after changes to compare.")
        return

    # Second run: ask for second file and compare
    second_file = input(
        "Enter the SECOND filename (e.g: after_update.txt): ").strip()
    services = get_services()
    save_services(services, second_file)

    print(f"\nComparing {first_file} and {second_file}...\n")
    old_services = set(load_services(first_file))
    new_services = set(load_services(second_file))

    added = sorted(new_services - old_services)
    removed = sorted(old_services - new_services)

    if not added and not removed:
        print("No changes in services detected.")
    else:
        if added:
            print("\n[+] New services added:")
            for svc in added:
                print(f"  {svc}")
                describe_service(svc)
        if removed:
            print("\n[-] Services removed:")
            for svc in removed:
                print(f"  {svc}")
                describe_service(svc)


if __name__ == "__main__":
    compare()
