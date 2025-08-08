#Elevate Lab Internship
#Task 3 :    Web Scraper for News Headlines
#Date: 7 Aug 2025
#Objective : Scrape top headlines from a news website
#================================================================================
import requests
from bs4 import BeautifulSoup

URL = "https://www.thehindu.com/news/national/"
response = requests.get(URL)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # we will find all <h3> tags which usually hold the headlines
    headlines = soup.find_all("h3")

    extracted_headlines = []
    for headline in headlines:
        text = headline.get_text(strip=True)
        if text and text not in extracted_headlines:
            extracted_headlines.append(text)

    # Saving the headlines with numbering
    with open("news_headlines.txt", "w", encoding="utf-8") as file:
        for idx, line in enumerate(extracted_headlines, start=1):
            file.write(f"{idx}. {line}\n")

    print(f"{len(extracted_headlines)} headlines saved to news_headlines.txt (with numbering)")
else:
    print(" Failed to fetch page.")
