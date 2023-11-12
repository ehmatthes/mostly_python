import os, sys, time
import requests

url = "https://on.substack.com/s/office-hours"

for attempt_num in range(90):
    r = requests.get(url)
    print(f"Attempt #{attempt_num}. Status: {r.status_code}")

    if " mins ago<" in r.text:
        cmd = f'open -a "Google Chrome" {url}'
        os.system(cmd)
        print("  Found a new post!")
        sys.exit()
    else:
        print("  No new post found. Waiting one minute...")
        time.sleep(60)