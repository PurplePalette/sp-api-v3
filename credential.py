import base64
import json

filename = input("Enter the credential filename >>")

try:
    with open(filename, "r", encoding="utf8") as f:
        cred = json.dumps(json.loads(f.read()))
    print("Please put below string as FIREBASE_CRED:")
    print(base64.b64encode(cred.encode()).decode())
except FileNotFoundError:
    print("Failed to load credential file.")
