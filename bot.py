import requests
from datetime import datetime

import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

CHAT_ID = "@namoz_vaqtlari_kanal"

OYLAR = ["yanvar", "fevral", "mart", "aprel", "may", "iyun", "iyul", "avgust", "sentyabr", "oktyabr", "noyabr", "dekabr"]

KUNLAR = ["dushanba", "seshanba", "chorshanba", "payshanba", "juma", "shanba", "yakshanba"]

def send(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    r=requests.post(url, json={"chat_id": CHAT_ID, "text": text})
    print(r.json())

bugun = datetime.now()
oy = OYLAR[bugun.month-1]
kun = KUNLAR[bugun.weekday()]
send(f"Assalomu alaykum, bugun {bugun.day}-{oy}, haftaning {kun} kuni. Kuningiz hayrli va barakali o'tsin!")