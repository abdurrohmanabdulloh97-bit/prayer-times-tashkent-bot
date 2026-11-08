import json
import re
import _json
import requests
from datetime import datetime
from playwright.sync_api import sync_playwright

import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

CHAT_ID = "@namoz_vaqtlari_kanal"
URL = "https://islom.uz/taqvim"

NAMOZLAR = {
    "Бомдод": "Bomdod",
    "Қуёш": "Quyosh",
    "Пешин": "Peshin",
    "Аср": "Asr",
    "Шом": "Shom",
    "Хуфтон": "Xufton",
}

def get_page_text():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=True)
        page=browser.new_page()
        page.goto(URL, wait_until="networkidle", timeout=60_000)
        page.wait_for_timeout(3_000)
        text=page.inner_text("body")
        browser.close()
    return text

def parse_times(text):
    times={}
    for sayt_nomi, nom in NAMOZLAR.items():
        m=re.search(sayt_nomi + r"[^\d]{0,40}?(?<![\d:])(\d{1,2}:\d{2})(?![\d:])", text)
        if m:
            times[nom]=m.group(1)
    return times

def send(text):
    url=f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    r=requests.post(url,data={"chat_id":CHAT_ID, "text": text}, timeout=15)
    print(r.status_code, r.text)

if __name__=="__main__":
    text=get_page_text()
    times=parse_times(text)
    print(json.dumps(times, ensure_ascii=False, indent=2))

    if len(times)<5:
        print("Vaqtlar topilmadi, sahifa matni:\n", text[:1500])
    else:
        bugun=datetime.now().strftime("%d.%m.%Y")
        xabar=f"🕌Bugungi namoz vaqtlari({bugun})\n\n"
        xabar+="\n".join(f"{n}:{t}" for n, t in times.items())
        xabar += "\n\n📍 Manba: islom.uz"
        send(xabar)

