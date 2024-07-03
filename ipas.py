from bs4 import BeautifulSoup
import requests



for index in range(1, 181):
    print(f"Scanning Page {index}/180")
    website = requests.get(f"https://ios-compatible.com/us/ipad-ios11/games/all/free/{index}/#content")
    scraper = BeautifulSoup(website.text, 'html.parser')

    data = scraper.find_all('div', attrs={"class": "row row-page-event"})
    for items in data:
        app_name = items.find('h3', attrs={"class": "mobile"}).text
        if "Rob" in app_name:
            print(f"App found on page {index}")
            break

