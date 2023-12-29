import requests
from bs4 import BeautifulSoup

def scrape_articles(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    articles = []
    for item in soup.find_all('a', class_='storylink'):
        articles.append({
            'title': item.get_text(),
            'url': item.get('href')
        })
    return articles

if __name__ == "__main__":
    articles = scrape_articles('https://news.ycombinator.com/')
    print(articles)
