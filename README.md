# 🔐 Password Generator

A command-line password generator built in Python that creates strong, cryptographically secure passwords and passphrases — with real entropy scoring and breach-time estimates.

## Features

- **Random password mode** — configurable length, mixed charset (letters, digits, symbols)
- **Passphrase mode** — 5-word passphrases from the EFF large wordlist (e.g. `paradox-water-cannabis-subsystem-elderly`)
- **Strength scoring** — powered by [zxcvbn](https://github.com/dwolfhub/zxcvbn-python), the same library used by Dropbox
- **Crack time estimate** — shows how long it would take to brute-force your password offline
- **Clipboard support** — auto-copies to clipboard when run outside Docker

## Why passphrases?

| Type | Example | Crack time |
|------|---------|------------|
| Short password (6 chars) | `ogZGWU` | 2 minutes |
| Common password | `Dog2019!` | 3 hours |
| Random password (20 chars) | `k#9Xm2!pQr...` | centuries |
| EFF passphrase (5 words) | `paradox-water-cannabis-subsystem-elderly` | centuries |

Passphrases are just as strong as random passwords — but actually memorable.

## Run with Docker (no installation needed)

```bash
docker run -it hiepnt2007/pwgen
```

## Run locally

**Install dependencies:**
```bash
pip install zxcvbn pyperclip
```

**Run:**
```bash
python pwgen.py
```

## Usage

```
🔐 Password Generator

1. Random password
2. Passphrase (easier to remember)

Pick a mode (1 or 2): 2

Your password:  paradox-water-cannabis-subsystem-elderly
Strength:       ████░ Strong (4/4)
Crack time:     centuries
✅ Copied to clipboard!
```

## Docker Hub

```bash
docker pull hiepnt2007/pwgen
```

## Tech stack

- Python 3.13
- [zxcvbn](https://github.com/dwolfhub/zxcvbn-python) — realistic password strength estimation
- [EFF Large Wordlist](https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt) — 7776 words
- Docker — published on Docker Hub

## Security notes

- Uses Python's `secrets` module (cryptographically secure), never `random`
- Passwords are never logged or stored
- Passphrase entropy: log₂(7776⁵) ≈ 64.6 bits
