import os
import json
import requests

# origin base URL
BASE_URL = "https://levelsharesquare.com/html5/supermarioconstruct/"

# local output directory
OUTPUT_DIR = "supermarioconstruct_assets"

# manifest file (downloaded offline.json first, or paste directly)
MANIFEST_FILE = "offline.json"

def download_file(url, dest):
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    try:
        r = requests.get(url, stream=True, timeout=30)
        r.raise_for_status()
        with open(dest, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        print(f"[OK] {url} -> {dest}")
    except Exception as e:
        print(f"[FAIL] {url} ({e})")

def main():
    # load manifest
    with open(MANIFEST_FILE, "r", encoding="utf-8") as f:
        manifest = json.load(f)

    # iterate through all listed files
    for rel_path in manifest.get("fileList", []):
        url = BASE_URL + rel_path
        dest = os.path.join(OUTPUT_DIR, rel_path.replace("/", os.sep))
        download_file(url, dest)

if __name__ == "__main__":
    main()