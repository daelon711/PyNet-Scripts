import threading
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_user_targets():  # gets websites from client
    print("\nEnter target **base URLs** (e.g., https://example.com)")
    print("Press Enter on an empty line to finish.\n")
    targets = []
    try:
        while True:
            url = input("URL: ").strip()
            if not url:
                break
            if not url.startswith("http"):
                url = "http://" + url  # default to http if missing
            targets.append(url.rstrip("/"))  # remove trailing slas
    except KeyboardInterrupt:
        print("\n[!] cancelled by user.")
    return targets


def scan_url(url, vuln_paths):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options=options)

    try:
        for path in vuln_paths:
            full_url = f"{url}{path}"
            try:
                driver.get(full_url)
                time.sleep(1)  # slight delay between requests
                if "404" not in driver.title.lower():
                    print(f"[!] endpoint found: {full_url}")
            except Exception as e:
                print(f"[!] Error accessing {full_url}: {e}")
        driver.quit()

    except Exception as e:
        print(f"[!] Error scanning URL {url}: {e}")
        driver.quit()


def path_scan():
    VULN_PATHS = [
        "/admin", "/login.php", "/config.php", "/data.php",
        "/phpinfo.php", "/test.php"
    ]

    targets = get_user_targets()
    if not targets:
        print("No targets entered...")
        return

    threads = []
    try:
        for url in targets:
            t = threading.Thread(target=scan_url, args=(url, VULN_PATHS))
            t.start()
            threads.append(t)
        for t in threads:
            t.join()

    except KeyboardInterrupt:
        print("\n[!] interrupted by user. Exiting...")
        return


if __name__ == "__main__":
    path_scan()
