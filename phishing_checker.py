"""Simple, text-only phishing URL awareness checks.

These heuristic checks identify warning signs; they cannot prove that a URL
is safe or malicious. The program never opens or visits submitted URLs.
"""
import ipaddress
from urllib.parse import urlparse


def analyze_url(url: str) -> list[str]:
    url = (url or "").strip()
    warnings = []

    if not url:
        return ["Please enter a URL."]

    candidate = url if "://" in url else "http://" + url
    parsed = urlparse(candidate)
    hostname = parsed.hostname or ""

    if not hostname:
        return ["The URL does not contain a recognizable hostname."]

    if "@" in url:
        warnings.append("The URL contains an @ symbol, which can hide the real destination.")

    if len(url) > 100:
        warnings.append("The URL is unusually long (over 100 characters).")

    try:
        ipaddress.ip_address(hostname)
        warnings.append("The hostname is an IP address instead of a familiar domain name.")
    except ValueError:
        pass

    if len(hostname.split(".")) >= 5:
        warnings.append("The hostname contains many subdomain segments.")

    if "xn--" in hostname.lower():
        warnings.append("The hostname contains an xn-- punycode marker.")

    if parsed.scheme.lower() == "http":
        warnings.append("The URL uses HTTP instead of HTTPS. HTTPS alone does not prove a site is trustworthy.")

    return warnings


def main():
    print("Phishing URL Awareness Checker")
    print("This tool checks URL text only. It does not visit URLs.")
    while True:
        url = input("\\nEnter a URL (or q to quit): ").strip()
        if url.lower() == "q":
            print("Goodbye.")
            break
        results = analyze_url(url)
        if results == ["Please enter a URL."]:
            print(results[0])
        elif results == ["The URL does not contain a recognizable hostname."]:
            print(results[0])
        elif results:
            print("\\nWarning signs:")
            for item in results:
                print("- " + item)
        else:
            print("No listed warning signs found. This does NOT mean the URL is safe.")


if __name__ == "__main__":
    main()
