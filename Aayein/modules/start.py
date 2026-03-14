from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ButtonStyle, ParseMode


@Client.on_message(filters.command("start") & filters.private)
async def start_handler(client, message):
    buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "➕ Add Account",
                    callback_data="add_account",
                    style=ButtonStyle.PRIMARY
                )
            ],
            [
                InlineKeyboardButton(
                    "❌ Delete Account",
                    callback_data="delete_account",
                    style=ButtonStyle.SUCCESS
                )
            ]
        ]
    )

    await message.reply_text(
        "⚡ <b>Account Manager Panel</b>\n\nChoose an option:",
        reply_markup=buttons,
        parse_mode=ParseMode.HTML
    )
