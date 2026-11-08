from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

async def on_post(update: Update, context: ContextTypes.DEFAULT_TYPE):
    post = update.channel_post
    name = post.author_signature or post.chat.title
    await post.reply_text(f"{name} kanalga yozdi")

app = Application.builder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.UpdateType.CHANNEL_POST, on_post))
app.run_polling()