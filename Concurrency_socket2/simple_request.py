import requests
import time

def download_site(url, session):
    with session.get(url) as response:
        print(f"Read {len(response.content)} from {url}")

def download_all_sites(sites):
    with requests.Session() as session: #사용후 세션 파일을 닫아 줌.
        for url in sites:
            download_site(url, session)

if __name__ == "__main__":
    sites = [
        "https://homepage.sch.ac.kr",
        "https://www.google.co.kr",
    ] * 80
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")
    