# Web3 Alert Bot

## Overview
Web3 Alert Bot is a Python-based Telegram bot that monitors Web3-related platforms (Medium and Mirror.xyz) for new articles and sends notifications to a Telegram chat.

## Features
- Scrapes the latest articles from Medium and Mirror.xyz.
- Sends new article notifications to a specified Telegram chat.
- Runs continuously and checks for new articles every 10 minutes.

## Requirements 
- Python 3.7+
- Telegram Bot API token 
- `requests`, `beautifulsoup4`, and `python-telegram-bot` packages
 
## Installation  
1. Clone the repository:     
   ```sh   
   git clone https://github.com/yourusername/Web3-Alert-Bot.git 
   cd Web3-Alert-Bot
   ``` 

2. Install dependencies:  
   ```sh
   pip install -r requirements.txt
   ``` 

3. Set up environment variables:
   ```sh
   export TELEGRAM_TOKEN='your-telegram-bot-token'
   export TELEGRAM_CHAT_ID='your-chat-id'
   ```

## Usage
Run the bot with:
```sh
python bot.py
```

## License
This project is licensed under the MIT License.
