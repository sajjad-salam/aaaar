import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic import app
from random import  choice, randint

#          
                
@app.on_message(filters.command(["الباشة","المبرمج الـبـاشـة","مبرمج السورس","مبرمج"],"")
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file-03-08-6",
        caption=f"""◉ 𝙽𝙰𝙼𝙴 : ❪[الـبـاشـة𐇮](https://t.me/G_D_U_VIP)❫
◉ 𝚄𝚂𝙴𝚁 : ❪ @G_D_U_VIP ❫
◉ 𝙸𝙳      : ❪ `733756075` ❫
◉ 𝙱𝙸𝙾    : ❪ for me (@G_D_U_VIP) my world (@N_9_N_6- @N_1_N_6) my bro (@G_D_U) ❫""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒𐇮 الـبـاشـة𐇮", url=f"https://t.me/G_D_U_VIP"), 
                 ],[
                   InlineKeyboardButton(
                        "الـبـاشـا", url=f"https://t.me/N_9_N_6"),
                ],

            ]

        ),

    )
