from pyrogram import Client, filters
from pyrogram.types import Message
from AylinRobot import AylinRobot as app

owner_idim = 6881891677

# Client oluşturma

# Bot sahibinin gruba katılması durumunda mesaj gönderen fonksiyon
@app.on_message(filters.new_chat_members)
def on_new_chat_members(client, message: Message):
    for user in message.new_chat_members:
        if user.id == owner_idim:
            # Bot sahibi gruba katıldığında mesaj gönder
            reply_message = message.reply("Salam Sahibim Xoş Gəldin Qrupa 🤖💙")
            # Emoji ve GIF eklemek için yanıt mesajına düzenleme yap
            reply_message.edit_text("salam Sahibim Xoş gəldin Qrupa 🤖💙😍")
            reply_message.reply_animation("https://telegra.ph/file/39a866819c72c9688f99c.mp4")
