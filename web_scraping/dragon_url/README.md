# Dragon URL Checker

This project is a Command Line Interface (CLI) tool designed to verify the connectivity status of any given website. It utilizes `argparse` for argument parsing and `requests` for connectivity checks, wrapped in a stylized "Dragon" theme with visual feedback.

## Files

- `dragon_url.py`
Main Python script. It parses command-line arguments to accept a target URL, performs an HTTP GET request, and visualizes the site's status (Online/Offline) using color-coded outputs.

## `dragon_checker.py (core logic)`

```
try:
    response = requests.get(args.url, timeout=5)

    if response.status_code == 200:
        p(colorama.Fore.LIGHTGREEN_EX + f'\n=🐉=🐉=🐉=🐉 SITE -> "{args.url}", STATUS -> ✅ =🐉=🐉=🐉=🐉\n' + colorama.Style.RESET_ALL)
    else:
        p(colorama.Fore.LIGHTRED_EX + f'\n=🐉=🐉=🐉=🐉 SITE -> "{args.url}", STATUS -> ❌ =🐉=🐉=🐉=🐉\n' + colorama.Style.RESET_ALL)

except requests.exceptions.RequestException:
    p(colorama.Fore.LIGHTRED_EX + f'\n=🐉=🐉=🐉=🐉 SITE -> "{args.url}", STATUS -> ❌ =🐉=🐉=🐉=🐉\n' + colorama.Style.RESET_ALL)
```

## What the script does

- Accepts a mandatory `--url` argument via the command line using `argparse`.
- Sends a GET request to the specified URL with a strict 5-second timeout to prevent hanging.
- Analyzes the HTTP status code:
    - Status 200: Marks the site as Online (✅).
    - Other Status / Errors: Marks the site as Offline (❌).
- Provides a robust CLI UX using `colorama` for typing effects (`p()` function) and bright, distinct colors for immediate visual feedback.

## Possible extensions

***You can extend this script to include features such as***:

- *Reading a list of URLs from a `.txt` file and checking them in batch*.

- *Logging the results (timestamp and status) to a local log file*.

- *Measuring and displaying the response time (latency) of the request*.

## Setup

If you are setting up this project for the first time, install the required libraries: `pip install requests colorama`
