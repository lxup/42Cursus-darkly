import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from tqdm import tqdm
import re

visited = set()
flag_found = False
progress_bar = None
flag_regex = re.compile(r"\b[a-f0-9]{64}\b", re.IGNORECASE)

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
        res = requests.get(url, timeout=3)
        res.raise_for_status()
    except Exception:
        return

    soup = BeautifulSoup(res.text, "html.parser")
    links = soup.find_all("a")

    print(f"Links ({len(links)}) found at {url}")
    for link in links:
        print(f"  - '{link.get('href', '')}'")
        if link.startswith("whtccjokayshttvxycsvykxcfm"):
            print("OKAAA")
        href = link.get("href")
        if not href or href in ("../", "./"):
            continue

        full_url = urljoin(url, href)

        if href == "README":
            if progress_bar:
                progress_bar.update(1)
            try:
                content = requests.get(full_url, timeout=3).text
                # /.hidden/whtccjokayshttvxycsvykxcfm/igeemtxnvexvxezqwntmzjltkt/lmpanswobhwcozdqixbowvbrhw/README"
                # show the content if the url is /.hidden/whtccjokayshttvxycsvykxcfm/igeemtxnvexvxezqwntmzjltkt/lmpanswobhwcozdqixbowvbrhw/README"
                flag = contains_flag(content)
                if flag:
                    print(f"\n🎉 [FLAG FOUND] at {full_url} 🎉")
                    print(flag)
                    flag_found = True
                    return
            except Exception:
                continue
        # else:
        #     crawl(full_url, depth + 1)

if __name__ == "__main__":
    root_url = "http://192.168.56.104/.hidden/"
    print("[*] Crawling recursively, please wait...")
    progress_bar = tqdm(total=20000, desc="Exploration", unit="dir", ncols=80)
    crawl(root_url)
    progress_bar.close()

    if not flag_found:
        print("❌ No flag found.")
