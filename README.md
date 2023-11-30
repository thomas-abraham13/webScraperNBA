# webScraperNBA
- Web scraping is the process of extracting and restructuring data from a website, usually to allow for some kind of eventual analysis. Aim of this project is to scrape NBA game data which can then further be used for various other projects.
- I used `requests` and `BeautifulSoup` to access the Basketball reference website and parse HTML.
- I'm using `pandas` to structure the information into a dataframe.

### nba_scrape.py uses nba_scraper:
This is a package written in Python to scrape the NBA's api and produce the play by play of games either in a csv file or a pandas dataframe. This package has two main functions scrape_game which scrapes an individual game or a list of specific games, and scrape_season which scrapes an entire season of regular season games.

### manual.ipynb:
This is a Jupyter notebook where I've attempted to scrape player data for the Boston Celtics using the Python libraries mentioned above.
