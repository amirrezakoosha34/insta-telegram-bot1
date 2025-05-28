import telebot
import requests
from config import 669342765:AAEFg-16hJKgkMx0AbBzKY7d1o7-PYqpv_g
, 418784159

bot = telebot.TeleBot(669342765:AAEFg-16hJKgkMx0AbBzKY7d1o7-PYqpv_g
)
welcome_message = "سلام! لینک اینستاگرام رو بفرست تا برات دانلودش کنم."

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, welcome_message)

@bot.message_handler(commands=['settext'])
def set_text(message):
    if message.from_user.id == 418784159:
        global welcome_message
        welcome_message = message.text.replace('/settext', '').strip()
        bot.reply_to(message, "✅ متن خوش‌آمدگویی با موفقیت تغییر کرد.")
    else:
        bot.reply_to(message, "⛔ شما دسترسی ندارید.")

@bot.message_handler(func=lambda message: True)
def download_instagram(message):
    url = message.text.strip()

    if "instagram.com" not in url:
        bot.reply_to(message, "❌ لطفا فقط لینک اینستاگرام بفرست.")
        return

    bot.send_chat_action(message.chat.id, 'typing')

    api_url = f"https://saveinsta.app/api/ajaxSearch"
    try:
        headers = {
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Referer": "https://saveinsta.app/",
        }
        data = {
            "q": url,
            "t": "media",
            "lang": "en"
        }
        response = requests.post(api_url, data=data, headers=headers)
        if response.status_code == 200 and 'url' in response.text:
            bot.send_message(message.chat.id, f"✅ لینک ارسال شد:
{url}")
        else:
            bot.send_message(message.chat.id, "⚠️ مشکلی در دریافت لینک پیش آمد.")
    except Exception as e:
        bot.send_message(message.chat.id, f"❌ خطا: {str(e)}")

bot.polling()
import time
while True:
    try:
        bot.polling()
    except Exception as e:
        print("Bot crashed, restarting...")
        time.sleep(5)
