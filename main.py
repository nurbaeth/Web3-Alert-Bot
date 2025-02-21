import os
import time
import requests
from bs4 import BeautifulSoup
from telegram import Bot

# Telegram Bot Token and Chat ID
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# URLs to monitor
MEDIUM_URL = "https://medium.com/tag/web3/latest"
MIRROR_URL = "https://mirror.xyz/"

# Initialize bot
bot = Bot(token=TELEGRAM_TOKEN)

# Function to fetch latest articles from Medium
def fetch_medium_articles():
    response = requests.get(MEDIUM_URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.find_all('h2')  # Medium articles titles
    links = [a.find_parent('a')['href'] for a in articles if a.find_parent('a')]
    return [(article.text, link) for article, link in zip(articles, links)]

# Function to fetch latest articles from Mirror
def fetch_mirror_articles():
    response = requests.get(MIRROR_URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.find_all('h3')  # Mirror article titles
    links = [a.find_parent('a')['href'] for a in articles if a.find_parent('a')]
    return [(article.text, link) for article, link in zip(articles, links)]

# Send message to Telegram
def send_telegram_message(message):
    bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)

# Main function
def main():
    last_articles = set()
    while True:
        new_articles = set(fetch_medium_articles() + fetch_mirror_articles())
        fresh_articles = new_articles - last_articles
        for title, link in fresh_articles:
            send_telegram_message(f"New Article: {title}\n{link}")
        last_articles = new_articles
        time.sleep(600)  # Check every 10 minutes

if __name__ == "__main__":
    main()
