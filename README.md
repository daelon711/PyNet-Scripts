# CyberOps Toolkit

A collection of small, standalone Python scripts covering common networking,
security-research, and general-utility tasks — built as a learning project.

> **Note:** most scripts are Linux-only. `mac_spoofing.py` and
> `service_comparator.py` specifically rely on Linux commands (`ip`,
> `systemctl`) and will not run on Windows or macOS.

## Project structure

```
.
├── docs/            # extra documentation / notes
├── screencast/       # demo recording
├── src/              # all the tool scripts + tests
└── requirements.txt
```

## Installation

1. Clone the repo and move into it:
   ```bash
   git clone <your-repo-url>
   cd <your-repo-name>
   ```
2. (Recommended) create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Linux system dependency needed for the file-type checker:
   ```bash
   sudo apt install libmagic1
   ```
5. First-time extras that download on first run:
   - `password_generator.py` downloads the NLTK `words` corpus the first time it's used.
   - `image_read.py` downloads EasyOCR's model weights the first time it's used (and needs a display for `image.show()`).

## Running the toolkit

Everything lives in `src/`, so run from there:

```bash
cd src
python main.py <tool_number>
```

Example: `python main.py 5` runs the port scanner.

### Available tools

| # | Tool |
|---|------|
| 1 | DDoS (simulation) |
| 2 | Password Generator |
| 3 | MAC Spoofing (Linux only) |
| 4 | Web Scraping |
| 5 | Port Scanner |
| 6 | Keylogger |
| 7 | Check File Type |
| 8 | Service Comparator (Linux only) |
| 9 | Paramiko SSH Command Execution |
| 10 | Glob → Regex Conversion |
| 11 | Endpoint Scanner |
| 12 | Email Validator / Builder |
| 13 | JSON Dumper (raw `http.client`) |
| 14 | Image Reader (OCR) |

`hostname_parser.py` isn't wired into `main.py` — it's a standalone script,
run directly:
```bash
python hostname_parser.py --hostname example.com
```

### Tests

A couple of the pure-logic helpers have unit tests:
```bash
cd src
pytest
```
- `test_ip.py` — validates `is_ip()` from `port_scanner.py`
- `test_email.py` — validates `is_valid_email()` from `email_utils.py`

## Screencast

If you want to hear the audio of the demo, open the video from the
`screencast/` folder in an actual media player rather than your IDE's
built-in preview. Video link:
https://drive.google.com/file/d/1_BAsRkO_Nkl8mlRk_geB7wk8KI4xNhlE/view?usp=sharing

## What each tool does

- **check_file_type** — uses `pathlib` and `magic` to detect a file's MIME
  type, and `send2trash` to optionally move suspicious files (executables,
  unknown binaries) to the trash instead of permanently deleting them.
- **ddos_attack** — simulation of an ICMP flood using `scapy`; includes
  helper functions (`is_ip`, domain resolution) that are reused/tested
  elsewhere in the project.
- **email_utils** — builds an `EmailMessage`, validates sender/recipient
  addresses with a regex, and prints the fully formatted email.
- **endpoint_scan** — uses Selenium (headless) and threading to check a list
  of common admin/config endpoints against user-supplied base URLs.
- **glob_to_re** — converts a glob pattern into its equivalent regex using
  `glob.translate`, then lets you test a string against it.
- **image_read** — opens an image with PIL and runs EasyOCR over it to pull
  out any text.
- **json_http** — fetches an API endpoint with the standard library's
  `http.client`, saves the JSON response to `api_response.json`, and offers
  to copy/move that file.
- **keylogger** — captures keystrokes while running and writes them to a
  file the user specifies.
- **mac_spoofing** — reads the active network interface via `ip route show`
  and assigns it a randomized MAC address (Linux only).
- **paramiko_study** — opens an SSH connection to another machine and runs a
  single command, printing the output.
- **password_generator** — builds a memorable-but-strong password from
  random dictionary words (via NLTK), digits, and a special character,
  retrying until it reaches 16+ characters.
- **port_scanner** — checks whether a port is open via a raw socket
  connection, or via an HTTP GET for a single port.
- **service_comparator** — snapshots the system's `systemctl` services to a
  file, then diffs a later snapshot against it to show what was added or
  removed (Linux only).
- **web_scraping** — fetches a URL with `requests` and `BeautifulSoup`, and
  either prints the full prettified page or just the text inside a specific
  tag.
- **hostname_parser** — resolves a hostname to an IP address via `argparse`
  + `socket`.

## Known limitations

- `paramiko_study.py` uses `AutoAddPolicy()`, which accepts unknown SSH host
  keys automatically — fine for a personal lab, not for anything exposed.
- `endpoint_scan.py` flags a path as "found" purely by checking whether
  `"404"` is absent from the page `<title>`, which is an unreliable signal
  on many real sites (custom error pages, SPAs, etc.).
- `service_comparator.py` and `mac_spoofing.py` shell out to Linux-specific
  commands and have no Windows/macOS equivalent.
