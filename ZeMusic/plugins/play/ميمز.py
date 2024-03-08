import asyncio
import config
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InputMediaVideo, InlineKeyboardMarkup, InlineKeyboardButton
from ZeMusic import app


@app.on_message(filters.command(["صرصار"], ""))
def mody(client, message):
    message.reply_photo(
        photo="https://graph.org/file/0331103b1c119716bad44.jpg",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("《🪳》", callback_data="mody")]])
    )

@app.on_callback_query(filters.command("mody"))
def modyy(client, callback_query):
    video = "https://telegra.ph/file-03-08-6"
    callback_query.edit_message_media(
        media=InputMediaVideo(media=video, caption=f"⚡هو المعفن اللى صحي الصرصار يجماعه😂👇\n\n{callback_query.from_user.first_name}")
    )
    
    
@app.on_message(filters.command(["خنزير"], ""))
def zeqe(client, message):
    message.reply_photo(
        photo="https://graph.org/file/c6234a6aedfbe638e0683.jpg",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("《🐖》", callback_data="modyl")]])
    )

@app.on_callback_query(filters.command("modyl"))
def zeqep(client, callback_query):
    video = "https://graph.org/file/274b6971aeb298bdcd6fe.mp4"
    callback_query.edit_message_media(
        media=InputMediaVideo(media=video, caption=f"⚡هو المعفن اللى صحي الخنزير يجماعه😂👇\n\n{callback_query.from_user.first_name}")
    )    
    
    
@app.on_message(filters.command(["نمله"], ""))
def namlo(client, message):
    message.reply_photo(
        photo="https://graph.org/file/bd1024b2f29996675596d.jpg",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("《🦗》", callback_data="modyll")]])
    )

@app.on_callback_query(filters.command("modyll"))
def namlop(client, callback_query):
    video = "https://graph.org/file/2d20cb201e06612588136.mp4"
    callback_query.edit_message_media(
        media=InputMediaVideo(media=video, caption=f"⚡هو المعفن اللى صحي النمله يجماعه😂👇\n\n{callback_query.from_user.first_name}")
    )        