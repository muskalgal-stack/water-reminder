import requests
import schedule
import time

TOKEN = "8350115582:AAHIzK0AhRhj2xLunrCD17a5oG07BgifaHM"
CHAT_ID = "6282530643"
MESSAGE = "היי מאמי 💧 רק מזכיר לך לשתות מים ושאני אוהב אותך ❤️"

def send_message():
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": MESSAGE})
    print("הודעה נשלחה!")

schedule.every().day.at("13:15").do(send_message)
schedule.every().day.at("16:00").do(send_message)
schedule.every().day.at("18:00").do(send_message)
schedule.every().day.at("20:00").do(send_message)

print("הבוט פועל...")
while True:
    schedule.run_pending()
    time.sleep(30)
