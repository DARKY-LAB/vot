from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ Cʀᴇᴀᴛᴏʀ: [DARKXSIDE78](https://t.me/Darkxside78)\n○ Lᴀɴɢᴜᴀɢᴇ: [Pʏᴛʜᴏɴ](https://www.python.org/downloads/)\n○ Lɪʙʀᴀʀʏ: [Pʏʀᴏɢʀᴀᴍ](https://github.com/pyrogram/pyrogram)\n○ Mᴀɪɴ Cʜᴀɴɴᴇʟ: [Gᴇɴ Aɴɪᴍᴇ](https://t.me/genanimeofc)\n○ Cʜᴀᴛ Gʀᴏᴜᴘ: [AɴɪCʜᴀᴛ](https://t.me/GenAnimeChat)\n○ Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ: [Bᴏᴛ Cʜᴀɴɴᴇʟ](https://t.me/+xp9acqFgosQ5NjNl)</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton("⚡️ ᴄʟᴏsᴇ", callback_data = "close"),
                    InlineKeyboardButton('🍁 ᴘʀᴇᴍɪᴜᴍ', url='https://t.me/GenAnimeOfc')
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
