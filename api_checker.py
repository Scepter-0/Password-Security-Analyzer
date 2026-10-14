import hashlib
import requests

def times_pwned(password):
    sha1 = hashlib.sha1(password.encode()).hexdigest().upper()
    prefix, suffix = sha1[:5], sha1[5:]
    response = requests.get(
        f"https://api.pwnedpasswords.com/range/{prefix}",
        headers={"User-Agent": "Password-Strength-Checker"},
        timeout=10,
    )
    response.raise_for_status()
    for line in response.text.splitlines():
        hash_suffix, count = line.split(":")
        if hash_suffix == suffix:
            return int(count)
    return 0

if __name__ == "__main__":
    password = input("Enter a password to check: ")
    count = times_pwned(password)
    print(f"\nThis password has appeared in {count} known data breaches.")