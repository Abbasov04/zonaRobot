# @AylinRobot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə Oğlum
# Reponu Satan Kodları Götürən Kimliyindən Aslı Olmayaraq Peysərdi

import os
import psutil
import shutil
import string
import asyncio
from AylinRobot.config import Config
from asyncio import TimeoutError
from AylinRobot.translation import Translation
from pyrogram import Client
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from AylinRobot.Plugin import *
from AylinRobot.Music import *
from AylinRobot.Oyunlar import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from AylinRobot import AylinRobot as app
from AylinRobot import LOGGER

AylinIMG = f"{Config.START_IMG}"

@app.on_message(filters.private & filters.incoming & filters.command(['start']))
async def start(client, message):
    await client.send_message(Config.LOG_CHANNEL,
        f"**🙋‍♀️ Yeni İstifadəçi**:\n\n**🙎‍♀️ Ad**: {message.from_user.mention}\n**🧟‍♀️ ID**:`{message.from_user.id}`\n**🌐 DC ID**: {message.from_user.dc_id}**\n📱 Telefon Nömrəsi**:{message.from_user.phone_number} \n**🇦🇿 DİL**: {message.from_user.language_code} \n**💁‍♀️ Bot**: [{Config.BOT_NAME}](https://t.me/{Config.BOT_USERNAME})")
    await message.reply_photo(
        AylinIMG,
        caption=Translation.START_TEXT.format(message.from_user.mention, Config.BOT_USERNAME,Config.OWNER_NAME, Config.BOT_NAME),
        reply_markup=Button.START_BUTTONS
    )
    
    
    
@app.on_message(filters.group & filters.incoming & filters.command(['start']))
async def gstart(client, message):
    await message.reply_photo(
        AylinIMG,
        caption=Translation.GSTART_TEXT.format(message.from_user.mention, Config.BOT_USERNAME, message.chat.title, Config.OWNER_NAME),
        reply_markup=Button.BAGLA_BUTTONS
    )      
    
    
@app.on_message(filters.group & filters.incoming & filters.command(['help']))
async def ghelp(client, message):
    await message.reply_photo(
        AylinIMG,
        caption=Translation.GHELP_TEXT.format(message.from_user.mention, Config.BOT_USERNAME, message.chat.title, Config.OWNER_NAME),
        reply_markup=Button.GHELP_BUTTONS
    )          
    

@app.on_message(filters.private & filters.incoming & filters.command(['help']))
async def ghelp(client, message):
    await message.reply_photo(
        AylinIMG,
        caption=Translation.PMHELP_TEXT.format(message.from_user.mention, Config.BOT_USERNAME, message.chat.title, Config.OWNER_NAME),
        reply_markup=Button.PMHELP_BUTTONS
    )          

    
    
@app.on_message(filters.new_chat_members, group=1)
async def hg(bot: Client, msg: Message):
    caption = await get_str(msg.chat.id)
    caption = caption(caption)
    for new_user in msg.new_chat_members:
        if new_user.id == Config.BOT_ID:
            await msg.reply(f"Ssss"
## HuseynH Əkən Pesi Dii
        elif new_user.id == Config.OWNER_ID:
            await msg.reply(f"Budur Sahibim Gəldi")    
    
    
    
app.start()
LOGGER.info(f"{Config.BOT_USERNAME} Uğurla Başladı Sahibim {Config.OWNER_NAME}")
idle()
