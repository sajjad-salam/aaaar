import asyncio
from pyrogram import Client, filters
from strings.filters import command
from ZeMusic.utils.decorators import AdminActual
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    InputMediaPhoto,
    Message,
)
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


REPLY_MESSAGE = "**- اهلا بك عزيزي اليك قائمه الاوامر**"




REPLY_MESSAGE_BUTTONS = [

         [

             ("‹ اوامر التشغيل ›"),                   

             ("‹ اوامر التفعيل ›")




          ],

          [

             ("‹ اوامر التسليه ›"),

             ("‹ السورس ›")

          ],

          [

             ("اخفاء الازرار")

          ]

]




  

@app.on_message(filters.regex("^الاوامر$"))
async def cpanel(_, message: Message):             
        text = REPLY_MESSAGE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, resize_keyboard=True, selective=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )

@app.on_message(filters.regex("اخفاء الازرار") & filters.group)
async def down(client, message):
          m = await message.reply("**- بخدمتك حجي خفيت الازرار\n- اذا تريد تطلعها مرة ثانية اكتب الاوامر**", reply_markup= ReplyKeyboardRemove(selective=True))


@app.on_message(filters.group & command("طريقة ربط القنوات"))
async def dowhmo(client: Client, message: Message):
    await message.reply_text("""- هلا والله\n◌**عشان تشغل بالقنوات لازم تسوي بعض الخطوات وهي◌** :\n\n1 -› تدخل البوت قناتك وترفعه مشرف\n2 -› ترجع للقروب وتكتب { **ربط + يوزر القناة** }\n3 -› **اضغط على زر اوامر التشغيل عشان تعرف كيف تشغل**..""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "قناة السورس", url=f"https://t.me/Source_Ze"),
                ],[
                    InlineKeyboardButton(
                        "• ضيفني لقروبك 🎻", url=f"https://t.me/{app.username}?startgroup=true"),
                ],
            ]
        ),
        disable_web_page_preview=True
    )
