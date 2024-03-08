import asyncio
import os
import time
import requests
import aiohttp
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic import app
from asyncio import gather


@app.on_message(filters.command(["تلغراف", "تلغراف ميديا", "ميديا", "تلجراف", "تليجراف"]) & filters.group)
async def telegraph(client: Client, message: Message):
    replied = message.reply_to_message
    if not replied:
        await message.reply("🤕 ¦ الرد على ملف وسائط مدعوم\n• حط صوره و اكتب عليها 00")
        return
    if not (
        (replied.photo and replied.photo.file_size <= 5242880)
        or (replied.animation and replied.animation.file_size <= 5242880)
        or (
            replied.video
            and replied.video.file_name.endswith(".mp4")
            and replied.video.file_size <= 5242880
        )
        or (
            replied.document
            and replied.document.file_name.endswith(
                (".jpg", ".jpeg", ".png", ".gif", ".mp4"),
            )
            and replied.document.file_size <= 5242880
        )
    ):
        await message.reply("غير مدعوم!!")
        return
    download_location = await client.download_media(
        message=message.reply_to_message,
        file_name="root/downloads/",
    )
    try:
        response = upload_file(download_location)
    except Exception as document:
        await message.reply(message, text=document)
    else:
        await message.reply(
            f"<b>• الــرابـط:-</b>\n\n <code>https://telegra.ph{response[0]}</code>",
            quote=True,
            reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="🎯 ¦ افـتح الـرابـط", url=f"https://telegra.ph{response[0]}"),
                    InlineKeyboardButton(text="♻️ ¦ مشـاركه الـرابـط", url=f"https://telegram.me/share/url?url=https://telegra.ph{response[0]}")
                ],
            ]
        )
    )
    finally:
        os.remove(download_location)





@app.on_message(filters.command(["معلوماته", "كشف"], "") & filters.group) 
async def hshs(client: Client, message: Message):      
    usr = await client.get_users(message.reply_to_message.from_user.id)
    name = usr.first_name#
    user_id = message.reply_to_message.from_user.id#
    chat_idd = message.chat.id#
    chat_username = f"@{message.chat.username}" #
    chat_name = message.chat.title#
    username = f"@{message.reply_to_message.from_user.username}"#
    async for photo in client.iter_profile_photos(message.reply_to_message.from_user.id, limit=1):
                    await message.reply_photo(photo.file_id,       caption=f"""**[★⌞ ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ ⌝˹⚡˼⁩](https://t.me/AlmortagelTech)\n\n🐉 ¦ ɴᴀᴍᴇ : {name}\n🤡 ¦ ᴜѕᴇ : {username}\n🔥 ¦ ɪᴅ : `{user_id}`\n🔅 ¦ ɪᴅ ᴄʜᴀᴛ : `{chat_idd}`\n💭 ¦ ᴄʜᴀᴛ : {chat_name}\n🐊 ¦ ɢʀᴏᴜᴘ : {chat_username} \n**""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{message.reply_to_message.from_user.username}")
                ],
            ]
        ),
    )     



@app.on_message(
    filters.command(["بايو","البايو"], "")
    & filters.group
    & filters.group
)
async def biio(client, message):
  nq = await client.get_chat(message.from_user.id)
  bio = nq.bio
  await message.reply_text(bio
  )
@app.on_message(
    filters.command(["شخصيتي", "معلوماتي", "شخصيه"], "")
    & filters.group
    & filters.group
)
async def ppdi(client: Client, message: Message):
    usr = await client.get_users(message.from_user.id)
    name = usr.first_name
    async for photo in client.iter_profile_photos(message.from_user.id, limit=1):
                    await message.reply_photo(photo.file_id,       caption=f"""**• انـت »   {message.from_user.mention()} يا قلبي ياناس🔥😮‍💨**""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        ),
    )
 
 
 
 
@app.on_message(filters.command(["تحويل_لصوره", "تحويل الصوره"], ""))
async def sticker_image(client: Client, message: Message):
    reply = message.reply_to_message
    if not reply:
        return await message.reply("الرد على ملصق.")
    if not reply.sticker:
        return await message.reply("الرد على ملصق.")
    m = await message.reply("يتم المعالجه..")
    f = await reply.download(f"{reply.sticker.file_unique_id}.png")
    await gather(*[message.reply_photo(f),message.reply_document(f)], "")
    await m.delete()
    os.remove(f)



@app.on_message(filters.command(["الجروب", "جروب"], "") & filters.group)
async def ginnj(client: Client, message: Message):
    chat_idd = message.chat.id
    chat_name = message.chat.title
    chat_username = f"@{message.chat.username}"
    photo = await client.download_media(message.chat.photo.big_file_id)
    await message.reply_photo(photo=photo, caption=f"""**🐲 ¦ الاسم » {chat_name}\n🚸 ¦ ايدي الجروب »  -{chat_idd}\n🐊 ¦ رابط » {chat_username}**""",     
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        chat_name, url=f"https://t.me/{message.chat.username}")
                ],
            ]
        ),
    )
    