from pathlib import Path
import magic
from send2trash import send2trash


def check_type():
    file_path = input(
        "Please enter the path to the file you want to check -> ").strip('"')
    valid, msg = check_if_file(file_path)
    if not valid:
        print(msg)
        return

    try:
        file_type = magic.from_file(file_path, mime=True)  # detect MIME type
        if file_type:
            print(f"Detected type: {file_type}")
        else:
            print("File type not detected. Showing first 8 bytes...")
            with open(file_path, 'rb') as file:
                first_8_bytes = file.read(8)
                print(f"In hex: {first_8_bytes.hex()}")
    except Exception as e:
        print(f"Cannot read file: {e}")
        return

    # ask user if they want to move suspicious file to trash
    suspicious_file(file_path, file_type)


def suspicious_file(file_path, file_type):
    suspicious_types = [
        "application/x-dosexec",
        "application/x-executable",
        "application/octet-stream"
    ]
    if file_type in suspicious_types or file_type is None:
        choice = input(
            "This file seems suspicious. Move it to trash? (y/n): ").lower()
        if choice == 'y':
            try:
                send2trash(str(file_path))
                print("File moved to trash")
            except Exception as trash_error:
                print(f"Could not move file to trash: {trash_error}")
        else:
            print("File not moved")


def check_if_file(file_path):
    file_pathed = Path(file_path)
    # check if the path exists and is a file
    if not file_pathed.exists():
        return False, f"{file_path} path does not exist"
    if not file_pathed.is_file():
        return False, f"{file_path} path is not a file"
    return True, None


if __name__ == "__main__":
    check_type()
