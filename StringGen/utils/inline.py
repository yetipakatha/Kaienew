from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import SUPPORT_CHAT


keyboard = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton(text="𝙂𝙚𝙣𝙚𝙧𝙖𝙩𝙚 𝙔𝙤𝙪𝙧 𝙨𝙩𝙧𝙞𝙣𝙜", callback_data="gensession")],
        [
            InlineKeyboardButton(text="𝙎𝙪𝙥𝙥𝙤𝙧𝙩", url=SUPPORT_CHAT),
        ],
    ]
)

gen_key = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="𝙋𝙮𝙧𝙤𝙜𝙧𝙖𝙢 𝙑1", callback_data="pyrogram1"),
            InlineKeyboardButton(text="𝙋𝙮𝙧𝙤𝙜𝙧𝙖𝙢 𝙑2", callback_data="pyrogram"),
        ],
        [InlineKeyboardButton(text="𝙏𝙚𝙡𝙚𝙩𝙝𝙤𝙣", callback_data="telethon")],
    ]
)

retry_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="𝙏𝙧𝙮 𝙖𝙜𝙖𝙞𝙣", callback_data="gensession")]]
)
