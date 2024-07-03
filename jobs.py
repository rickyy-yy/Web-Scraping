import requests
import csv
from bs4 import BeautifulSoup

site = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation="
data = requests.get(site)
scraper = BeautifulSoup(data.text, 'lxml')

jobs = scraper.find_all('li', attrs={"class": "clearfix job-bx wht-shd-bx"})
for job in jobs:
    date_posted = job.find('span', attrs={"class": "sim-posted"}).span.text
    if "few" in date_posted:

        employer = job.find('h3', attrs={"class": "joblist-comp-name"}).text.replace(' ', '')
        skills = job.find('span', attrs={"class": "srp-skills"}).text.replace(' ', '')
        job_url = job.header.h2.a['href ']
        print(f"Company Name: {employer.strip()}")
        print(f"Skills: {skills.strip()}")
        print(f"URL: {job_url}")
        print("")
