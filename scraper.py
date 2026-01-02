import requests
from bs4 import BeautifulSoup
import csv

URL = "https://quotes.toscrape.com/"

def scrape_quotes():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")

    quotes = soup.find_all("div", class_="quote")

    data = []

    for quote in quotes:
        text = quote.find("span", class_="text").text
        author = quote.find("small", class_="author").text
        tags = [tag.text for tag in quote.find_all("a", class_="tag")]

        data.append([text, author, ", ".join(tags)])

    with open("quotes.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Quote", "Author", "Tags"])
        writer.writerows(data)

    print("Quotes scraped and saved to quotes.csv")

if __name__ == "__main__":
    scrape_quotes()
