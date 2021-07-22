#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ ADMIN : <a href='tg://user?id={OWNER_ID}'>Pencet Ini</a>\n○ Creator : @ibraipin\n○ Channel : @Virtualmeresahkan1\n○ Support Group : @Virtualmeresahkan18</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("OKE", callback_data = "OKE")
                    ]
                ]
            )
        )
    elif data == "OKE":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
