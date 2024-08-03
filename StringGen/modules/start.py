from pyrogram import filters
from pyrogram.types import Message
from config import START_IMG_URL
from StringGen import Anony
from StringGen.utils import add_served_user, keyboard


@Anony.on_message(filters.command("start") & filters.private & filters.incoming)
async def f_start(_, message: Message):
    response = await message.reply_photo(
        photo=START_IMG_URL,
        caption=f"𝙃𝙚𝙮 {message.from_user.first_name},\n\n 𝙄'𝙢 {Anony.mention},\n 𝙖 𝙢𝙤𝙨𝙩 𝙩𝙧𝙪𝙨𝙩𝙖𝙗𝙡𝙚 𝙨𝙩𝙧𝙞𝙣𝙜 𝙨𝙚𝙨𝙨𝙞𝙤𝙣 𝙜𝙚𝙣𝙚𝙧𝙖𝙩𝙤𝙧 𝙛𝙧𝙤𝙢 𝙩𝙝𝙚 𝙘𝙧𝙚𝙖𝙩𝙤𝙧𝙨 𝙤𝙛 𝙪𝙣𝙞𝙫𝙚𝙧𝙨𝙚 𝙣𝙚𝙩𝙬𝙤𝙧𝙠 𝙮𝙤𝙪 𝙘𝙖𝙣 𝙜𝙚𝙩 𝙗𝙤𝙩𝙝 𝙩𝙚𝙡𝙚𝙩𝙝𝙤𝙣 𝙖𝙣𝙙 𝙥𝙮𝙧𝙤𝙜𝙧𝙖𝙢 𝙨𝙚𝙨𝙨𝙞𝙤𝙣 𝙛𝙧𝙤𝙢 𝙢𝙚 𝙖𝙣𝙙 𝙞𝙛 𝙮𝙤𝙪 𝙝𝙖𝙫𝙚 𝙖𝙣𝙮 𝙞𝙨𝙨𝙪𝙚𝙨 𝙞𝙣 𝙜𝙚𝙩𝙩𝙞𝙣𝙜 𝙨𝙩𝙧𝙞𝙣𝙜 𝙧𝙚𝙖𝙘𝙝 𝙢𝙮 𝙨𝙪𝙥𝙥𝙤𝙧𝙩 𝙜𝙧𝙤𝙪𝙥.",
        reply_markup=keyboard
    )
    await add_served_user(message.from_user.id)
