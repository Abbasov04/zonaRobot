# © Naviya2

import asyncio
from AylinRobot.config import Config
from pyrogram import Client
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message


async def ForceSub(bot: Client, event: Message):
    """
@HuseynH tərəfindən Xüsusi Piroqram Əsaslı Telegram Botunun Məcburi Abunə Funksiyası.
     İstifadəçi Mesaj Göndərmək üçün Alt Kanal Botuna Qoşulmayıbsa və Ondan Əvvəlcə Qoşulmasını xahiş et.
     """
    
    try:
        invite_link = await bot.create_chat_invite_link(chat_id=(int(Config.UPDATES_CHANNEL)))
    except FloodWait as e:
        await asyncio.sleep(e.x)
        fix_ = await ForceSub(bot, event)
        return fix_
    except Exception as err:
        print(f"{Config.UPDATES_CHANNEL} kanalına məcburi abunə olmaq mümkün deyil\n\nXəta: {err}\n\nSahibimlə Əlaqə Saxla [HÜSEYN](https://t.me/{Config.OWNER_NAME}) Deyin.:")
        return 200
    try:
        user = await bot.get_chat_member(chat_id=(int(Config.UPDATES_CHANNEL)), user_id=event.from_user.id)
        if user.status == "kicked":
            await bot.send_message(
                chat_id=event.from_user.id,
                text=f"Üzr istəyirik, əzizim, məndən istifadə etmək qadağandır ☹️\nSahibimlə Əlaqə Saxla [HÜSEYN](https://t.me/{Config.OWNER_NAME}) deyin.",
                parse_mode="markdown",
                disable_web_page_preview=True,
                reply_to_message_id=event.message_id
            )
            return 400
        else:
            return 200
    except UserNotParticipant:
        await bot.send_message(
            chat_id=event.from_user.id,
            text="<b>Salam</b> {},\n\n<b>Sən hələ də Playlist Kanalıma Qoşulmamısan ☹️ \nPlaylist Kanalıma, Qoşulun Və 'Yenilə 🔄' Düyməsinə Toxun</b>".format(event.from_user.mention),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🎵 Playlist", url=f"https://t.me/{Config.PLAYLIST_NAME}"),
                    ],

                    [   
                        InlineKeyboardButton("Yenilə 🔄", callback_data="refreshme")
                    ],
                ]
            ),
            parse_mode="HTML",
            reply_to_message_id=event.message_id
        )
        return 400
    except FloodWait as e:
        await asyncio.sleep(e.x)
        fix_ = await ForceSub(bot, event)
        return fix_
    except Exception as err:
        print(f"Nə isə səhv getdi!  Məcburi Abunə olmaq mümkün deyil.\nXəta: {err}\n\nSahibim [HÜSEYN](https://t.me/{Config.OWNER_NAME}) İlə Əlaq Saxla",
        return 200
