from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Channel", url="https://t.me/Dolatghavi_IranGhavi")],
        [InlineKeyboardButton(
            "Report Bugs 😊", url="https://t.me/Rezaaf76")]
    ])
    welcomed = f"سلام <b>{message.from_user.first_name}</b> را بزنید\n/help برای اطلاعات بیشتر "
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
