from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"لینک مربوط به ویدیو رو برای ما ارسال کنید."
    await message.reply_text(helptxt)
