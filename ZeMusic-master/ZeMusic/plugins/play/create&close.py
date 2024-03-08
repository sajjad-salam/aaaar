import asyncio
from typing import Optional
from random import randint
from pyrogram.types import Message, ChatPrivileges
from pyrogram import Client, filters
from strings.filters import command
from pyrogram.raw.functions.channels import GetFullChannel
from pyrogram.raw.functions.messages import GetFullChat
from pyrogram.raw.types import InputGroupCall, InputPeerChannel, InputPeerChat
from ZeMusic.utils.database import *
from pyrogram.raw.functions.phone import CreateGroupCall, DiscardGroupCall
from pyrogram.errors import UserAlreadyParticipant, UserNotParticipant, ChatAdminRequired
from ZeMusic import app , Userbot

async def get_group_call(
    client: Client, message: Message, err_msg: str = ""
) -> Optional[InputGroupCall]:
    assistant = await get_assistant(message.chat.id)
    chat_peer = await assistant.resolve_peer(message.chat.id)
    if isinstance(chat_peer, (InputPeerChannel, InputPeerChat)):
        if isinstance(chat_peer, InputPeerChannel):
            full_chat = (
                await assistant.invoke(GetFullChannel(channel=chat_peer))
            ).full_chat
        elif isinstance(chat_peer, InputPeerChat):
            full_chat = (
                await assistant.invoke(GetFullChat(chat_id=chat_peer.chat_id))
            ).full_chat
        if full_chat is not None:
            return full_chat.call
    await app.send_message(f"**No group call Found** {err_msg}")
    return False

@app.on_message(filters.regex("^افتح المكالمه$"))
async def start_group_call(c: Client, m: Message):
    chat_id = m.chat.id
    assistant = await get_assistant(chat_id)
    ass = await assistant.get_me()
    assid = ass.id
    if assistant is None:
        await app.send_message(chat_id, "خطأ في المساعد")
        return
    msg = await app.send_message(chat_id, "جاري تشغيل المكالمه..")
    try:
        peer = await assistant.resolve_peer(chat_id)
        await assistant.invoke(
            CreateGroupCall(
                peer=InputPeerChannel(
                    channel_id=peer.channel_id,
                    access_hash=peer.access_hash,
                ),
                random_id=assistant.rnd_id() // 9000000000,
            )
        )
        await msg.edit_text("تم فتح المكالمه بنجاح ⚡️~!")
    except ChatAdminRequired:
      try:    
        await app.promote_chat_member(chat_id, assid, privileges=ChatPrivileges(
                can_manage_chat=False,
                can_delete_messages=False,
                can_manage_video_chats=True,
                can_restrict_members=False,
                can_change_info=False,
                can_invite_users=False,
                can_pin_messages=False,
                can_promote_members=False,
            ),
        )
        peer = await assistant.resolve_peer(chat_id)
        await assistant.invoke(
            CreateGroupCall(
                peer=InputPeerChannel(
                    channel_id=peer.channel_id,
                    access_hash=peer.access_hash,
                ),
                random_id=assistant.rnd_id() // 9000000000,
            )
        )
        await app.promote_chat_member(chat_id, assid, privileges=ChatPrivileges(
            can_manage_chat=False,
            can_delete_messages=False,
            can_manage_video_chats=False,
            can_restrict_members=False,
            can_change_info=False,
            can_invite_users=False,
            can_pin_messages=False,
            can_promote_members=False,
            ),
        )                              
        await msg.edit_text("تم فتح المكالمه بنجاح ⚡️~!")
      except:
         await msg.edit_text("خلي البوت معاه صلاحية اضافة مشرفين والتحكم ف المحادثه الصوتيه او خلي الاك المساعد رول وجرب ⚡")
@app.on_message(filters.regex("^اقفل المكالمه$"))
async def stop_group_call(c: Client, m: Message):
    chat_id = m.chat.id
    assistant = await get_assistant(chat_id)
    ass = await assistant.get_me()
    assid = ass.id
    if assistant is None:
        await app.send_message(chat_id, "خطأ في المساعد")
        return
    msg = await app.send_message(chat_id, "جاري اغلاق المكالمه..")
    try:
        if not (
           group_call := (
               await get_group_call(assistant, m, err_msg=", group call already ended")
           )
        ):  
           return
        await assistant.invoke(DiscardGroupCall(call=group_call))
        await msg.edit_text("تم اغلاق المكالمه بنجاح ⚡️~!")
    except Exception as e:
      if "GROUPCALL_FORBIDDEN" in str(e):
       try:    
         await app.promote_chat_member(chat_id, assid, privileges=ChatPrivileges(
                can_manage_chat=False,
                can_delete_messages=False,
                can_manage_video_chats=True,
                can_restrict_members=False,
                can_change_info=False,
                can_invite_users=False,
                can_pin_messages=False,
                can_promote_members=False,
             ),
         )
         if not (
           group_call := (
               await get_group_call(assistant, m, err_msg=", group call already ended")
           )
         ):  
           return
         await assistant.invoke(DiscardGroupCall(call=group_call))
         await app.promote_chat_member(chat_id, assid, privileges=ChatPrivileges(
            can_manage_chat=False,
            can_delete_messages=False,
            can_manage_video_chats=False,
            can_restrict_members=False,
            can_change_info=False,
            can_invite_users=False,
            can_pin_messages=False,
            can_promote_members=False,
            ),
         )                              
         await msg.edit_text("تم اغلاق المكالمه بنجاح ⚡️~!")
       except:
         await msg.edit_text("خلي البوت معاه صلاحية اضافة مشرفين والتحكم ف المحادثه الصوتيه او خلي الاك المساعد عنده صلاحية رفع مشرفين وجرب")
    
