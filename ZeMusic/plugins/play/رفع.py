import time
import asyncio
from config import OWNER_ID
from pyrogram import Client, filters
from ZeMusic import app
import random
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait
lokrf = []

@app.on_message(
     command(["قفل الرفع","تعطيل الرفع"])
     & filters.group

   
)
async def iddlock(client:Client, message:Message):
    dev = (OWNER_ID)
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if message.from_user.id in dev:
        rotba = "مطور اساسي"
    elif get.status in [ChatMemberStatus.OWNER]:
        rotba= "المــــــألك"
    elif get.status in [ChatMemberStatus.ADMINISTRATOR]:
        rotba= "أدمــــــن"
    else:   
        return await message.reply_text(f"**يا {message.from_user.mention} انت لست مشرفا هنا**")    
     
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] and  dev:
        if message.chat.id in lokrf:
            return await message.reply_text(f"**يا {message.from_user.mention}\n الالعاب مقفله من قبل**")
        lokrf.append(message.chat.id)
        return await message.reply_text(f"**تم قفل الالعاب بنجاح\n\n بواسطة {rotba} ←{message.from_user.mention}**")
    else:
        return await message.reply_text(f"**يا {message.from_user.mention} انت لست مشرفا هنا**")

@app.on_message(
    command(["فتح الرفع","تفعيل الرفع"])
    & filters.group
)
async def idljjopen(client:Client, message:Message):
    dev = (OWNER_ID)
  
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if message.from_user.id in dev:
        rotba = "مطـور اساسي"
    elif get.status in [ChatMemberStatus.OWNER]:
        rotba= "المــــألك"
    elif get.status in [ChatMemberStatus.ADMINISTRATOR]:
        rotba= "أدمـــن"
    else:
        return await message.reply_text(f"**يا {message.from_user.mention} انت لست مشرف هنا**")       
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] and  dev:
      if not message.chat.id in lokrf:
        return await message.reply_text(f"**يا {message.from_user.mention}\الالعاب مفعله من قبل**")
      lokrf.remove(message.chat.id)
      return await message.reply_text(f"**تم فتح الالعاب بنجاح\n\n بواسطة {rotba} ←{message.from_user.mention}**")
 
   


klb = []

@app.on_message(command("رفع مميز"))
async def rf3nmla(client:Client, message:Message):
  
  if message.reply_to_message.from_user.mention in klb:
    klb.append(message.reply_to_message.from_user.mention)
  await message.reply_text(f"**تم رفع العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n مميز من قبل {message.from_user.mention}**")


@app.on_message(command("تنزيل مميز"))
async def tnzelnmla(client:Client, message:Message):
  if message.reply_to_message.from_user.mention in klb:
    klb.remove(message.reply_to_message.from_user.mention)
  await message.reply_text(f"**تم تنزيل العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n من قائمة المميزين  \n\n لعرض القائمه اكتب `المميزين`**")


@app.on_message(command("المميزين"))
async def nml(client:Client, message:Message):
  kq = ""
  for n in klb:
      kq += n + "\n"
  await message.reply_text(f"**قائمة المميزين  \n\n{kq}**")

zoj = []


@app.on_message(command("رفع ادمن"))
async def rf3nmla(client, message:Message):
  if message.reply_to_message.from_user.mention in zoj:
    zoj.append(message.reply_to_message.from_user.mention)
  await message.reply_text(f"**تم رفع العضو\n│ \n : {message.reply_to_message.from_user.mention}\n\n  ادمن من قبل {message.from_user.mention}\n\n لعرض القائمه اكتب `الادمنيه`**")


@app.on_message(command("تنزيل ادمن"))
async def tnzelnmla(client:Client, message:Message):
  if message.reply_to_message.from_user.mention in zoj:
    zoj.remove(message.reply_to_message.from_user.mention)
  await message.reply_text(f"**تم تنزيل العضو\n│ \n : {message.reply_to_message.from_user.mention}\n\n من قائمة الادمنيه **")


@app.on_message(command("الادمنيه"))
async def nml(client, message):
  zq = ""
  for n in zoj:
      zq += n + "\n"
  await message.reply_text(f"**قائمه الادمنيه :  \n {zq}**")

hth =[]


@app.on_message(command("رفع مدير"))
async def rf3nmla(client, message:Message):
  
  if message.reply_to_message.from_user.mention in hth:
    hth.append(message.reply_to_message.from_user.mention)
  await message.reply_text(f"**تم رفع العضو\n│ \n : {message.reply_to_message.from_user.mention}\n\n  مدير من قبل {message.from_user.mention}\n\n لعرض القائمه اكتب `المدراء`**")


@app.on_message(command("تنزيل مدير"))
async def tnzelnmla(client:Client, message:Message):
  if message.reply_to_message.from_user.mention in hth:
    hth.remove(message.reply_to_message.from_user.mention)
  await message.reply_text(f"**تم تنزيل العضو\n│ \n : {message.reply_to_message.from_user.mention}\n\n من قائمة المدراء اكتب `المدراء` **")


@app.on_message(command("المدراء"))
async def nml(client, message):
  hq = ""
  for n in hth:
      hq += n + "\n"
  await message.reply_text(f"**قائمه المدراء  : \n {hq}**")


zog =[]


@app.on_message(command("رفع منشى"))
async def rf3nmla(client, message:Message):
  if message.reply_to_message.from_user.mention in zog:
    zog.append(message.reply_to_message.from_user.mention)
  await message.reply_text(f"**تم رفع العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n  منشى من قبل : {message.from_user.mention} \n\n لعرض القائمه اكتب `المنشئين`**")


@app.on_message(command("تنزيل منشى"))
async def tnzelnmla(client:Client, message:Message):
  if message.reply_to_message.from_user.mention in zog:
    zog.remove(message.reply_to_message.from_user.mention)
  await message.reply_text(f"**تم تنزيل العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n  من قائمه المنشئين **")


@app.on_message(command("المنشئين"))
async def nml(client:Client, message:Message):
  zzq = ""
  for n in zog:
      zzq += n + "\n"
  await message.reply_text(f"**قائمة المنشئين :  \n {zzq}**")
