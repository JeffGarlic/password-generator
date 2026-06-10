import secrets
import string
import pyperclip
from zxcvbn import zxcvbn
import urllib.request

def generate_password(length=20):
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return "".join(secrets.choice(chars) for _ in range(length))

def get_eff_wordlist():
    url = "https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt"
    words = []
    with urllib.request.urlopen(url) as response:
        for line in response.read().decode().splitlines():
            parts = line.strip().split("\t")
            if len(parts) == 2:
                words.append(parts[1])
    return words

def generate_passphrase(words=5):
    wordlist = get_eff_wordlist()
    return "-".join(secrets.choice(wordlist) for _ in range(words))

def strength_bar(score):
    bars = ["░░░░░", "█░░░░", "██░░░", "███░░", "████░", "█████"]
    labels = ["Very weak", "Weak", "Fair", "Good", "Strong", "Very strong"]
    return bars[score], labels[score]

def main():
    print("\n🔐 Password Generator\n")
    print("1. Random password")
    print("2. Passphrase (easier to remember)")
    choice = input("\nPick a mode (1 or 2): ").strip()

    if choice == "1":
        length = input("Length? (default 20): ").strip()
        length = int(length) if length.isdigit() else 20
        pw = generate_password(length)
    elif choice == "2":
        pw = generate_passphrase()
    else:
        print("Invalid choice.")
        return

    result = zxcvbn(pw)
    score = result["score"]
    bar, label = strength_bar(score)
    crack_time = result["crack_times_display"]["offline_slow_hashing_1e4_per_second"]

    print(f"\nYour password:  {pw}")
    print(f"Strength:       {bar} {label} ({score}/4)")
    print(f"Crack time:     {crack_time}")

    try:
        pyperclip.copy(pw)
        print("\n✅ Copied to clipboard!")
    except Exception:
        print("\n(Clipboard not available in Docker — copy the password manually)")

if __name__ == "__main__":
    main()