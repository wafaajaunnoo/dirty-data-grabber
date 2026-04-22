import requests

def fetch_page(url):
    response = requests.get(url)
    return response.text

if __name__ == "__main__":
    print(fetch_page("https://httpbin.org/html"))