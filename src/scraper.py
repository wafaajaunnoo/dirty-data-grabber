import time
import random
import requests

def fetch_page(url, retries=3):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
    }
    for attempt in range(retries):
        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt+1} failed: {e}")
            if attempt <retries -1:
                wait = (2 ** attempt) + random.uniform(0,1)
                print(f"Retrying in {wait:.2f} seconds")
                time.sleep(wait)
            else:
                raise

    return None

if __name__ == "__main__":
    print(fetch_page("https://httpbin.org/html"))