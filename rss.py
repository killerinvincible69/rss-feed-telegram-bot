import os
import sys
import feedparser
from sql import db
from time import sleep, time
from dotenv import load_dotenv
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from apscheduler.schedulers.background import BackgroundScheduler


if os.path.exists("config.env"):
    load_dotenv("config.env")


try:
    api_id = int(os.environ.get("API_ID"))   # Get it from my.telegram.org
    api_hash = os.environ.get("API_HASH")   # Get it from my.telegram.org
    feed_urls = list(set(i for i in os.environ.get("FEED_URLS").split("|")))  # RSS Feed URL of the site.
    feed_urls2 = list(set(i for i in os.environ.get("FEED_URLS2").split("|")))
    feed_urls3 = list(set(i for i in os.environ.get("FEED_URLS3").split("|")))
    feed_urls4 = list(set(i for i in os.environ.get("FEED_URLS4").split("|")))
    bot_token = os.environ.get("BOT_TOKEN")   # Get it by creating a bot on https://t.me/botfather
    log_channel = int(os.environ.get("LOG_CHANNEL"))   # Telegram Channel ID where the bot is added and have write permission. You can use group ID too.
    check_interval = int(os.environ.get("INTERVAL", 10))   # Check Interval in seconds.  
    max_instances = int(os.environ.get("MAX_INSTANCES", 3))   # Max parallel instance to be used.
except Exception as e:
    print(e)
    print("One or more variables missing. Exiting !")
    sys.exit(1)


for feed_url in feed_urls:
    if db.get_link(feed_url) == None:
        db.update_link(feed_url, "*")


app = Client(":memory:", api_id=api_id, api_hash=api_hash, bot_token=bot_token)


def create_feed_checker(feed_url):
    def check_feed():
        FEED = feedparser.parse(feed_url)
        entry = FEED.entries[0]
        if entry.id != db.get_link(feed_url).link:
                       # ↓ Edit this message as your needs.
            message = f"/mirror@Mirror_by_invinci_bot ```{entry.link}``\n**{entry.title}** "
            try:
                app.send_message(log_channel, message)
                db.update_link(feed_url, entry.id)
            except FloodWait as e:
                print(f"FloodWait: {e.x} seconds")
                sleep(e.x)
            except Exception as e:
                print(e)
        else:
            print(f"Checked RSS FEED: {entry.id}")
    return check_feed


scheduler = BackgroundScheduler()
for feed_url in feed_urls:
    feed_checker = create_feed_checker(feed_url)
    scheduler.add_job(feed_checker, "interval", seconds=check_interval, max_instances=max_instances)
scheduler.start()

for feed_url2 in feed_urls2:
    if db.get_link(feed_url2) == None:
        db.update_link(feed_url2, "*")


app = Client(":memory:", api_id=api_id, api_hash=api_hash, bot_token=bot_token)


def create_feed_checker2(feed_url2):
    def check_feed2():
        FEED2 = feedparser.parse(feed_url2)
        entry2 = FEED2.entries[0]
        if entry2.id != db.get_link(feed_url2).link:
                       # ↓ Edit this message as your needs.
            message = f"/mirror@Mirrorxinvincible3_bot ```{entry2.link}``\n**{entry2.title}** "
            try:
                app.send_message(log_channel, message)
                db.update_link(feed_url2, entry2.id)
            except FloodWait as e:
                print(f"FloodWait: {e.x} seconds")
                sleep(e.x)
            except Exception as e:
                print(e)
        else:
            print(f"Checked RSS FEED: {entry2.id}")
    return check_feed2


scheduler = BackgroundScheduler()
for feed_url2 in feed_urls2:
    feed_checker2 = create_feed_checker2(feed_url2)
    scheduler.add_job(feed_checker2, "interval", seconds=check_interval, max_instances=max_instances)
scheduler.start()

for feed_url3 in feed_urls3:
    if db.get_link(feed_url3) == None:
        db.update_link(feed_url3, "*")


app = Client(":memory:", api_id=api_id, api_hash=api_hash, bot_token=bot_token)


def create_feed_checker3(feed_url3):
    def check_feed3():
        FEED3 = feedparser.parse(feed_url3)
        entry3 = FEED3.entries[0]
        if entry3.id != db.get_link(feed_url3).link:
                       # ↓ Edit this message as your needs.
            message = f"/mirror@Mirrorxinvinci_bot ```{entry3.link}``\n**{entry3.title}** "
            try:
                app.send_message(log_channel, message)
                db.update_link(feed_url3, entry3.id)
            except FloodWait as e:
                print(f"FloodWait: {e.x} seconds")
                sleep(e.x)
            except Exception as e:
                print(e)
        else:
            print(f"Checked RSS FEED: {entry3.id}")
    return check_feed3


scheduler = BackgroundScheduler()
for feed_url3 in feed_urls3:
    feed_checker3 = create_feed_checker3(feed_url3)
    scheduler.add_job(feed_checker3, "interval", seconds=check_interval, max_instances=max_instances)
scheduler.start()

for feed_url4 in feed_urls4:
    if db.get_link(feed_url4) == None:
        db.update_link(feed_url4, "*")


app = Client(":memory:", api_id=api_id, api_hash=api_hash, bot_token=bot_token)


def create_feed_checker4(feed_url4):
    def check_feed4():
        FEED4 = feedparser.parse(feed_url4)
        entry = FEED4.entries[0]
        if entry.id != db.get_link(feed_url4).link:
                       # ↓ Edit this message as your needs.
            message = f"/mirror2 ```{entry.link}``\n**{entry.title}** "
            try:
                app.send_message(log_channel, message)
                db.update_link(feed_url4, entry.id)
            except FloodWait as e:
                print(f"FloodWait: {e.x} seconds")
                sleep(e.x)
            except Exception as e:
                print(e)
        else:
            print(f"Checked RSS FEED: {entry.id}")
    return check_feed4


scheduler = BackgroundScheduler()
for feed_url4 in feed_urls4:
    feed_checker4 = create_feed_checker4(feed_url4)
    scheduler.add_job(feed_checker4, "interval", seconds=check_interval, max_instances=max_instances)
scheduler.start()

app.run()
