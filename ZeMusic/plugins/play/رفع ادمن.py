import asyncio
import os
import time
import requests
import aiohttp
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic import app
from asyncio import gather
from pyrogram.errors import FloodWait

@app.on_message(filters.command("رفع ادمن", ""))
def promote_admin(client, message):
    if message.reply_to_message and message.reply_to_message.from_user:
        target = message.reply_to_message.from_user.id
        user_id = str(target)
    elif message.reply_to_message is None:
        target = message.text.split()[2]
        user = app.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            message.reply_text("لا يمكن العثور على المستخدم")
            return
    else:
        target = message.text.split()[1].strip("@")
        user = app.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            message.reply_text("لا يمكن العثور على المستخدم")
            return

    chat_id = str(message.chat.id)
    tom_admin = load_tom_admin()

    if (not TOM(client, message, message) and not basic_dev(client, message, message) and not OWNER_ID(client, message, message) and not dev(client, message, message) and not is_basic_creator(client, message, message) and not owner(client, message, message) and not creator(client, message, message)):
        message.reply_text("""◍ يجب ان تكون منشئ على الاقل لكى تستطيع رفع ادمن
√""")
        return

    if chat_id not in tom_admin['admin']:
        tom_admin['admin'][chat_id] = {'admin_id': []}

    if user_id in tom_admin['admin'][chat_id]['admin_id']:
        message.reply_text("""◍ هذا المستخدم ادمن بالفعل
√""")
    else:
        tom_admin['admin'][chat_id]['admin_id'].append(user_id)
        dump_tom_admin(tom_admin)
        message.reply_text("""◍ تم رفع المستخدم ليصبح ادمن
√""")




@app.on_message(filters.command("تنزيل ادمن", ""))
def demote_admin(client, message):
    if message.reply_to_message and message.reply_to_message.from_user:
        target = message.reply_to_message.from_user.id
        user_id = str(target)
    elif message.reply_to_message is None:
        target = message.text.split()[2]
        user = app.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            message.reply_text("لا يمكن العثور على المستخدم")
            return
    else:
        target = message.text.split()[1].strip("@")
        user = app.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            message.reply_text("لا يمكن العثور على المستخدم")
            return
    chat_id = str(message.chat.id)
    

    tom_admin = load_tom_admin()
    if (not TOM(client, message, message) and not basic_dev(client, message, message) and not OWNER_ID(client, message, message) and not dev(client, message, message) and not is_basic_creator(client, message, message) and not owner(client, message, message) and not creator(client, message, message)):
        message.reply_text("""◍ يجب ان تكون منشئ على الاقل لكى تستطيع تنزيل ادمن
√""")
        return
    if chat_id not in tom_admin['admin']:
        message.reply_text("لا يوجد مشرفين حتى الأن")
        return

    if user_id not in tom_admin['admin'][chat_id]['admin_id']:
        message.reply_text("""◍ هذا المستخدم ليس ادمن لتنزيله
√""")
    else:
        tom_admin['admin'][chat_id]['admin_id'].remove(user_id)
        dump_tom_admin(tom_admin)
        message.reply_text("""◍ تم تنزيل المستخدم من الادمن بنجاح
√""")



@app.on_message(filters.command("مسح الادمنيه", ""))
def clear_admins(client, message):
    chat_id = str(message.chat.id)
    tom_admin = load_tom_admin()
    if (not TOM(client, message, message) and not basic_dev(client, message, message) and not OWNER_ID(client, message, message) and not dev(client, message, message) and not is_basic_creator(client, message, message) and not owner(client, message, message) and not creator(client, message, message)):
        message.reply_text("""◍ يجب ان تكون منشئ على الاقل لستخدام الامر
√""")
        return
    if chat_id in tom_admin['admin']:
        tom_admin['admin'][chat_id]['admin_id'] = []
        dump_tom_admin(tom_admin)
        message.reply_text("""◍ تم مسح الادمنيه بنجاح
√""")
    else:
        message.reply_text("لا يوجد ادمنيه ليتم مسحهم")






@app.on_message(filters.command("الادمنيه", ""))
def get_admins(client, message):
    chat_id = str(message.chat.id)
    tom_admin = load_tom_admin()

    if chat_id not in tom_admin['admin']:
        message.reply_text("لا يوجد مشرفين في هذه الدردشة")
        return

    admins = tom_admin['admin'][chat_id]['admin_id']
    if not admins:
        message.reply_text("لا يوجد مشرفين في هذه الدردشة")
    else:
        admin_names = []
        for admin_id in admins:
            user = app.get_users(int(admin_id))
            if user:
                admin_names.append(f"[{user.first_name}](tg://user?id={user.id})")

        
        if admin_names:
            admin_list = "\n".join(admin_names)
            message.reply_text(f"◍ قائمة المشرفين:\n\n{admin_list}")
        else:
            message.reply_text("تعذر العثور على معلومات المشرفين")

