import asyncio

import os
import time
import requests
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic import app
from random import  choice, randint

                
@app.on_message(
    command(["سورس","‹ السورس ›","سورس","السورس", "سورس"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file-03-08-6",
        caption=f"""**ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ . .
 [الـبـاشـة](https://t.me/N_9_N_6)**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "المطور", url=f"https://t.me/G_D_U"), 
                    
                
                    InlineKeyboardButton(
                        "‹ الدعم ›", url=f"https://t.me/G_D_U_VIP"),
                ],[
                    
                
                    InlineKeyboardButton(
                        "‹ السورس ›", url=f"https://t.me/N_9_N_6"),
                
        ],

            ]

        ),

    )

