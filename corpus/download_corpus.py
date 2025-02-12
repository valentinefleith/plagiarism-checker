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


def main():
    all_links = get_all_dissertation_links()
    print(all_links)


if __name__ == "__main__":
    main()
