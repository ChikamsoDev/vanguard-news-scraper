import csv
import time

import requests
from bs4 import BeautifulSoup


URL = "https://www.vanguardngr.com/"


with open("vanguard_headlines.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Date"])

    response = requests.get(URL, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "lxml")

    articles = soup.find_all("article", class_="entry-card")

    for article in articles:
        anchor = article.find("h3", class_="entry-title").find("a")
        date_tag = article.find("div", class_="entry-date")

        title = anchor.text.strip()
        date = date_tag.text.strip() if date_tag else "No date"

        writer.writerow([title, date])
        print(f"{title} | {date}")

time.sleep(1)