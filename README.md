# EWB Phishing URL Awareness Checker

## Overview
This Python project checks URL text for selected phishing warning signs. It does not open URLs or send data anywhere.

## Features
- Detects an `@` symbol
- Flags URLs longer than 100 characters
- Flags an IPv4 address as hostname
- Flags hostnames with five or more dot-separated parts
- Flags punycode marker (`xn--`)
- Flags HTTP scheme
- Repeats checks until `q` is entered
- Handles malformed URL text without opening a website

## Requirements
Python 3.10 or later. No extra packages.

## How to Run
Windows: `python phishing_checker.py` (or `py phishing_checker.py`)
Mac/Linux: `python3 phishing_checker.py`

## Testing
Run all five sample URLs in `tests/test_samples.md`. Record actual output and PASS/FAIL honestly.

## Screenshots
Save your genuine screenshots as `screenshots/sample_run.png` and `screenshots/test_results.png`.

## Improvements
1. Repeats URL checks in one session and exits with `q`.
2. Handles malformed URL input with a clear message.

## Limitations
This is an educational tool, not a definitive phishing detector. It checks only six visible patterns. No warning signs found does not mean a URL is safe, and HTTPS alone does not prove trust.

## Ethical Use
Use only fictional sample strings. Do not open suspicious links, collect credentials, send phishing messages, or probe websites without written authorisation.

## Author
Replace this line with your name and batch/course before publishing.
