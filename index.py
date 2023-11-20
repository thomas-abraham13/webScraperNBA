import requests
from bs4 import BeautifulSoup

# URL of the website you want to scrape
URL = 'https://example.com'

# Send an HTTP request to the URL
response = requests.get(URL)

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
    
