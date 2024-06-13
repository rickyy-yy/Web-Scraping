from bs4 import BeautifulSoup
import requests
import csv

website = requests.get("http://quotes.toscrape.com")
scraper = BeautifulSoup(website.text, "html.parser")

quotes = scraper.findAll("span", attrs={"class": "text"})
authors = scraper.findAll("small", attrs={"class": "author"})

file_path = "C:\\Users\\yourf\\Documents\\data.csv"

with open(file_path, 'w') as file:
    writer = csv.writer(file)
    writer.writerow(["Quotes", "Author"])
    for quote, author in zip(quotes, authors):
        writer.writerow([quote.text, author.text])
