"""
webScraper for the official NBA website
"""

import platform
import requests
from bs4 import BeautifulSoup
import nba_scraper.nba_scraper as ns

# URL of the website to scrape
URL = 'https://www.nba.com/'

# Send an HTTP request to the URL
response = requests.get(URL , timeout=10)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find specific elements on the page by their HTML tags, classes, IDs, etc.
    # For example, let's find all the links (anchor tags) on the page
    links = soup.find_all('a')

    # Print out the href attribute of each link
    for link in links:
        print(link.get('href'))
else:
    print('Failed to retrieve the webpage')

# Setup a data directory based on the user's OS
if platform.system() == 'Darwin':
    LOC='/Users/thomasabraham/Projects/webScraperNBA/scraped_data'
elif platform.system() == 'Windows':
    LOC=''
else:
    LOC=''

# all nba game ids have two leading zeros but you can omit these
nba_df = ns.scrape_game([21800001, 21800002])
ns.scrape_game([21800001, 21800002], data_format='csv', data_dir=LOC)
