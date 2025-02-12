import os
import requests
from bs4 import BeautifulSoup as bs


URL = "https://www.20aubac.fr"
MAIN_PAGE_URL = f"{URL}/sujets/philosophie-dissertation"


def get_all_dissertation_links():
    response = requests.get(MAIN_PAGE_URL)
    soup = bs(response.text, "html.parser")
    links = soup.find_all("a")
    all_links = [
        f"{URL}{link['href']}"
        for link in links
        if link["href"].startswith("/corriges/")
    ]
    return all_links


def get_content(url):
    response = requests.get(url)
    soup = bs(response.text, "html.parser")
    if "Obtenir un accès premium" in soup.text:
        return None
    return "".join(
        [p.get_text().replace("\xa0", " ") for p in soup.find_all("p")][1:-5]
    )


def save_content_as_file(content, link):
    CORPUS_DIR = "corpus/raw"
    if not os.path.exists(CORPUS_DIR):
        os.makedirs(CORPUS_DIR)
    name = f"{CORPUS_DIR}/{link.split('/')[-1]}.txt"
    with open(name, "w") as f:
        f.write(content)


def main():
    all_links = get_all_dissertation_links()
    for link in all_links:
        content = get_content(link)
        if content is None:
            continue
        # print(content)
        print("Downloading", link)
        save_content_as_file(content, link)
    # print(all_links)


if __name__ == "__main__":
    main()
