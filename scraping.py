import requests
from bs4 import BeautifulSoup
import csv

def scraping(url):
    try:
        # Send a GET request to the news website
        res = requests.get(url)
        res.raise_for_status()  # Raise an error for bad responses

        # Parse the HTML content in a structured manner
        soup = BeautifulSoup(res.text, 'html.parser')

        # Find the headlines and links (modify the selectors based on the website structure)
        headlines = []
        for item in soup.find_all('h3'):  # Adjust the tag and class based on the site
            headline = item.get_text(strip=True)
            link = item.find('a')['href'] if item.find('a') else None

            if link and not link.startswith('http'):
                link = url + link  # Handle relative links

            headlines.append({'headline': headline, 'link': link})

        return headlines

    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def save_to_csv(data, filename='headlines.csv'):
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['headline', 'link'])
        writer.writeheader()
        writer.writerows(data)

if __name__ == '__main__':
    news_url = input("Enter the URL: ")  # Replace with the desired news site
    news_headlines = scraping(news_url)

    if news_headlines:
        save_to_csv(news_headlines)
        print(f"Saved {len(news_headlines)} headlines to headlines.csv")
    else:
        print("No headlines found.")
