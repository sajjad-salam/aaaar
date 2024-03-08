import asyncio
import pyrogram
import random
import datetime
from ZeMusic import app
from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Message
from pyrogram import Client, filters
from pyrogram.types import ChatMemberUpdated, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.types import (InlineKeyboardButton,

                            InlineKeyboardMarkup, Message)






@app.on_message(filters.regex(r'حساب العمر'))
async def calculate_age(client, message):
    try:
        birth_date = datetime.datetime.strptime(message.text.split(" ")[2], "%d-%m-%Y")
    except:
        await message.reply_text("خطأ عزيزي برجاء ادخال تاريخ ميلادك بهذه الصيغه مثال - ( 1994-1-1 )")
        return

    today = datetime.datetime.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    months = (today.year - birth_date.year) * 12 + today.month - birth_date.month
    days = (today - birth_date).days
    next_birthday = datetime.datetime(today.year, birth_date.month, birth_date.day)
    if today > next_birthday:
        next_birthday = datetime.datetime(today.year+1, birth_date.month, birth_date.day)
    remaining_days = (next_birthday - today).days

    await message.reply_text(f" • عمرك هو >> {age} سنه\n\n  •عمرك ب الاشهر >> {months} شهر \n\n  •عمرك ب الايام >> {days} يوم.\n\n  •عيد ميلادك بعد >> {remaining_days} يوم.")
