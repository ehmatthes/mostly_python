import os, sys, time
import requests


class OOMonitor:

    def __init__(self, url, target_string, num_attempts=90):
        self.url = url
        self.target_string = target_string
        self.num_attempts = num_attempts

    def start_monitoring(self):
        for attempt_num in range(self.num_attempts):
            r = requests.get(self.url)
            print(f"Attempt #{attempt_num}. Status: {r.status_code}")

            if target_string in r.text:
                cmd = f'open -a "Google Chrome" {url}'
                os.system(cmd)
                print("  Found a new post!")
                sys.exit()
            else:
                print("  No new post found. Waiting one minute...")
                time.sleep(60)

if __name__ == '__main__':
    url = "https://on.substack.com/s/office-hours"
    target_string = " min ago<"
    target_string = "Oct 26"

    monitor = OOMonitor(url, target_string)
    monitor.start_monitoring()