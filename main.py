import requests
from bs4 import BeautifulSoup
from datetime import datetime

def fetch_yahoo_japan_news():
    url = "https://news.yahoo.co.jp/"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    now = datetime.now().strftime('%Y-%m-%d')
    print(f"📅 {now} のYahoo日本ニュース：\n")

    items = soup.select("a.sc-1nhdoj2-1")

    count = 0
    for item in items:
        title = item.get_text(strip=True)
        link = item['href']
        print(f"- {title}")
        print(f"  🔗 {link}")
        count += 1
        if count >= 10:
            break

if __name__ == "__main__":
    fetch_yahoo_japan_news()
