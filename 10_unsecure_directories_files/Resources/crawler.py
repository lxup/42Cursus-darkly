import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from tqdm import tqdm
import re

visited = set()
flag =
progress_bar = None
flag_regex = re.compile(r"\b[a-f0-9]{64}\b", re.IGNORECASE)
session = requests.Session()

def contains_flag(text):
    for word in text.split():
        if flag_regex.fullmatch(word):
            return word
    return None

def crawl(url, depth=0):
    global progress_bar, flag_found


    if url in visited or flag_found:
        return
    visited.add(url)

    try:
        res = session.get(url, timeout=3)
        res.raise_for_status()
    except Exception as e:
        print(f"❌ Failed to access {url} → {type(e).__name__}: {e}")
        return

    soup = BeautifulSoup(res.text, "html.parser")
    links = soup.find_all("a")

    for link in links:
        href = link.get("href")
        if not href or href in ("../", "./"):
            continue

        full_url = urljoin(url, href)

        if href == "README":
            if progress_bar:
                progress_bar.update(1)
            try:
                content = requests.get(full_url, timeout=3).text
                flag = contains_flag(content)
                if flag:
                    print(f"\n🎉 [FLAG FOUND] at {full_url} 🎉")
                    print(f"====> {flag} <====")
                    flag_found = True
                    return
            except Exception:
                continue
        elif href.endswith("/"):
            crawl(full_url, depth + 1)

if __name__ == "__main__":
    root_url = "http://192.168.56.104/.hidden/"
    print("[*] Crawling recursively, please wait...")
    progress_bar = tqdm(total=18279, desc="Exploration", unit="dir", ncols=80)
    crawl(root_url)
    progress_bar.close()

    if not flag_found:
        print("❌ No flag found.")
