from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("کانال اسپانسر ما", url="https://t.me/rezaafsh")],
        [InlineKeyboardButton(
            "اطلاع مشکل", url="https://t.me/Rezaaf76")]
    ])
    welcomed = f"سلام <b>{message.from_user.first_name}</b> عزیز\n برای راهنمایی روی /help بزن\nبا عضویت در کانال زیر از من حمایت کنید.\n @rezaafsh"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
