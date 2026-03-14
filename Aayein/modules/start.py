from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Aayein import bot


@bot.on_message(filters.command("start"))
async def start_handler(client, message):

    buttons = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("➕ Add Account", callback_data="add_account")],
            [InlineKeyboardButton("❌ Delete Account", callback_data="delete_account")]
        ]
    )

    await message.reply_text(
        "⚡ **Welcome to Account Manager Bot**",
        reply_markup=buttons
    )
