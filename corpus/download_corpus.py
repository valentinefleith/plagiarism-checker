import os
import requests
from bs4 import BeautifulSoup as bs


URL = "https://www.20aubac.fr"
MAIN_PAGE_URL = f"{URL}/sujets/philosophie-"


def get_all_links(exercise_type: str):
    response = requests.get(f"{MAIN_PAGE_URL}{exercise_type}")
    soup = bs(response.text, "html.parser")
    links = soup.find_all("a")
    all_links = [
        f"{URL}{link['href']}"
        for link in links
        if link["href"].startswith("/corriges/")
    ]
    return all_links


def get_content(url, exercise_type):
    response = requests.get(url)
    soup = bs(response.text, "html.parser")
    if "Obtenir un accès premium" in soup.text:
        return None
    if exercise_type == "dissertation":
        return "".join(
            [p.get_text().replace("\xa0", " ") for p in soup.find_all("p")][1:-5]
        )
    return "".join(
        [p.get_text().replace("\xa0", " ") for p in soup.find_all("p")][3:-5]
    )


def save_content_as_file(content, link, exercise_type):
    CORPUS_DIR = f"corpus/{exercise_type}"
    if not os.path.exists(CORPUS_DIR):
        os.makedirs(CORPUS_DIR)
    name = f"{CORPUS_DIR}/{link.split('/')[-1]}.txt"
    with open(name, "w") as f:
        f.write(content)


def get_subject_name(link, exercise_type):
    response = requests.get(link)
    soup = bs(response.text, "html.parser")
    if "Obtenir un accès premium" in soup.text:
        return None
    if exercise_type == "dissertation":
        return soup.find("title").text.strip()


def save_subjects(subjects: list):
    with open("sujets_dissert.txt", "w") as outf:
        for subject in subjects:
            outf.write(subject + "\n")


def main():
    types = ["dissertation", "commentaire"]
    subjects = []
    for exercise_type in types:
        all_links = get_all_links(exercise_type)
        for link in all_links:
            content = get_content(link, exercise_type)
            if content is None:
                continue
            subject = get_subject_name(link, exercise_type)
            subjects.append(subject)
            print("Downloading", link)
            save_content_as_file(content, link, exercise_type)
    save_subjects(subjects)


if __name__ == "__main__":
    main()
