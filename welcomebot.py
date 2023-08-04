from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext, ConversationHandler

# Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your actual Telegram bot token
BOT_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'

def start(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    welcome_message = f"🟢 Zipple Mod\n\n- Available Filters : /tax ,/twitter ,/lock ,/renounce ,/website ,/whitepaper ,/roadmap ,/ca \n\n- Useful links on the group !"
    buttons = [
        [InlineKeyboardButton("🌎 Website", url="https://zipple.online")],
        [InlineKeyboardButton("📜 Whitepaper", url="https://docs.zipple.online")],
        [InlineKeyboardButton("🛣 Roadmap", url="https://docs.zipple.online/roadmap")],
        [InlineKeyboardButton("✖️ Twitter", url="https://twitter.com/zippletoken")],
        [InlineKeyboardButton("🅿️ Github", url="https://github.com/zipplecommunity")],
        [InlineKeyboardButton("⏺ LP Lock", url="https://t.me/zipplecommunity")],
        [InlineKeyboardButton("♻️ CA Renounce", url="https://t.me/zipplecommunity")],
        [InlineKeyboardButton("🤖 Zipple bot", url="https://docs.zipple.online/zipple-telegram-bots")]
    ]

    reply_markup = InlineKeyboardMarkup(buttons)
    update.message.reply_text(welcome_message, reply_markup=reply_markup)

def main():
    updater = Updater(token=BOT_TOKEN)
    dispatcher = updater.dispatcher

    # Use MessageHandler with Filters.status_update.new_chat_members to handle new members joining the group
    dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_members, start))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
