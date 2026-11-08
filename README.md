 # Prayer times in Tashkent telegram bot

A Python bot that gets daily prayer times from [islom.uz](https://islom.uz) and posts them to a Telegram channel every day at 20:00.

## Setup

1. Install dependencies: pip install -r requirements.txt
2. Create a bot with @BotFather and copy its token.
3. Create a .env file: BOT_TOKEN=your_token
4. Add the bot as an admin to your channel.

## Run

python scraper_bot.py

The daily 00:00 run is scheduled with Task Scheduler (Windows) or cron (Linux).

Source: islom.uz