import asyncio
from ZeMusic import app 
from strings.filters import command
import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


italy = ["انت اللي مين ؟!", "بتكلمني انا", "معرفش🤔", "اللي ضاع من عمرو سنين نيهه😹", "انت متعرفنيش بجد اخص علي الصحب؟!"]

@app.on_message(filters.text & filters.regex(r"(^|\W)مين(\W|$)"))
async def Italymusic(client, message):
    if "مين" in message.text:
        response = random.choice(italy)
        keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("قناة السورس", url="https://t.me/N_9_N_6")]])
        await message.reply(response, reply_markup=keyboard)

