# Elevate Lab Internship
## Task 3: Web Scraper for News Headlines.
## Objective:  Scrape top headlines from a news website.
## Tools : Python, requests, BeautifulSoup
### Below are the points which I learned from this project

- 📰 The Hindu News Headlines Scraper <br>
&nbsp;&nbsp;This Python script automatically collects the latest national news headlines from The Hindu newspaper’s National News section and saves them into a .txt file with numbering.

- 🔧 Tools & Libraries Used <br>
&nbsp;&nbsp;Python (Programming Language)<br>
&nbsp;&nbsp;requests – For sending HTTP requests to fetch the webpage<br>
&nbsp;&nbsp;beautifulsoup4 – For parsing HTML and extracting the headlines<br>

- 📂 Project Files<br>
&nbsp;&nbsp;news_scraper.py – Main Python script that scrapes the headlines.<br>
&nbsp;&nbsp;news_headlines.txt – Output file containing the scraped headlines.<br>

🚀 How It Works<br>
&nbsp;&nbsp;-The program starts by opening the National News page of The Hindu newspaper through code.<br>
&nbsp;&nbsp;-It uses the web address: https://www.thehindu.com/news/national/<br>
&nbsp;&nbsp;-The requests library sends a request to get the webpage content.<br>
&nbsp;&nbsp;-The program checks if the website responded successfully (status code 200).<br>
&nbsp;&nbsp;-The BeautifulSoup library reads the HTML code of the webpage.<br>
&nbsp;&nbsp;-It searches for all h3 tags that contain news headlines.<br>
&nbsp;&nbsp;-Each headline is cleaned to remove extra spaces and avoid duplicates.<br>
&nbsp;&nbsp;-The program numbers each headline for better readability.<br>
&nbsp;&nbsp;-All headlines are saved into a file called news_headlines.txt.<br>
&nbsp;&nbsp;-Finally, it shows a message with the number of headlines saved.<br>
