# News Scraper

**The News Scraper is a Python script designed to scrape the latest headlines and their corresponding links from a specified news website. The extracted data is organized and saved in either JSON or CSV format. The script is built to handle potential issues such as missing or malformed HTML elements gracefully.**


## Features
- Scrapes latest news headlines and links.
- Outputs data in JSON and CSV formats.
- Handles missing or malformed HTML elements gracefully.
## Prerequisites

- Python 3.x
- The following Python libraries:
  
  - `requests` - for making HTTP requests
  - `beautifulsoup4` - for parsing HTML
  - `pandas` - for handling CSV data
- Install the required libraries using:
  ```bash
  pip install requests beautifulsoup4 

### ***Sample URL:***
  ##### '''https://indianexpress.com/''
## Sample Output
``` 
      Enter the URL: https://indianexpress.com/
      Saved 50 headlines to headlines.csv
