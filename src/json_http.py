import http.client
import json
import shutil
from pathlib import Path


def handle_file(path):

    action = input(
        "if you want to (c)opy, (m)ove, or (n)othing with the file [c/m/n]: ").lower()
    if action in ('c', 'm'):
        dest = input("destination path: ")
        dest = Path(dest)
        if not dest.parent.exists():
            print("destination directory doesn't exist")
            return
        try:
            if action == 'c':
                shutil.copy(path, dest)
                print(f"File copied to {dest}")
            elif action == 'm':
                shutil.move(path, dest)
                print(f"File moved to {dest}")
        except Exception as e:
            print(f"failed: {e}")
    else:
        print("Nothing was performed")


def fetch_api_data():
    host = input(
        "Enter API host (e.g., jsonplaceholder.typicode.com): ").strip()
    endpoint = input("Enter API endpoint (e.g., /todos/1): ").strip()

    try:
        conn = http.client.HTTPSConnection(host)
        conn.request("GET", endpoint)
        response = conn.getresponse()

        print(f"Status: {response.status} {response.reason}")
        if response.status != 200:
            print("[!] API did not return 200 OK")
            return

        # Read and decode response
        data = response.read().decode("utf-8")

        try:
            json_data = json.loads(data)
        except json.JSONDecodeError:
            print("[!] Response is not valid JSON")
            return
        path = "api_response.json"
        # Write to file
        with open(path, "w") as f:
            json.dump(json_data, f, indent=4)
        print("JSON data saved to 'api_response.json'")
        handle_file(path)

    except Exception as e:
        print(f"Connection error: {e}")


if __name__ == '__main__':
    fetch_api_data()
