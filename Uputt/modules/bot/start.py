# if you can read this, this meant you use code from Geez | Ram Project
# this code is from somewhere else
# please dont hestitate to steal it
# because Geez and Ram doesn't care about credit
# at least we are know as well
# who Geez and Ram is
#
#
# kopas repo dan hapus credit, ga akan jadikan lu seorang developer
# ©2023 Geez | Ram Team
import random
from Uputt import app
from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from config import OWNER_ID as owner 

@app.on_callback_query()
def pmowner(client, callback_query):
    user_id = owner
    message = "Lu Siapa Anjeng!!!!"
    client.send_message(user_id, message)
    client.answer_callback_query(callback_query.id, text="Message sent")

logouputt = [
    "https://telegra.ph/file/7d7432a542a03ded9ae43.jpg",
    "https://telegra.ph/file/0400c0b0b2d9869d3a9d5.jpg",
    "https://telegra.ph/file/737fceed0883e53576b13.jpg",
    "https://telegra.ph/file/de157ee8f1053273de9a1.jpg"
]

alive_logo = random.choice(logouputt)

@app.on_message(filters.command("start") & filters.private)
async def start(app, message):
    chat_id = message.chat.id
    file_id = alive_logo
    caption = "Hi, Saya Asisstant Bee-Pyrobot\nTidak Ada Yang Special Kecuali Bee."
    reply_markup = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Support", url="https://t.me/cari_kawanindonesia"),
            InlineKeyboardButton("Channel", url="https://t.me/BeeXDomp"),
        ],
    ])

    await app.send_photo(chat_id, file_id, caption=caption, reply_markup=reply_markup)
