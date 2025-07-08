import telebot

BOT_TOKEN = "7810086473:AAFz23CjhKmLMmkuiRop_vuAaTOy9DtRP9A"
bot = telebot.TeleBot(BOT_TOKEN)

# /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 
        "👋 Hi bro! Welcome to *Ghibli Style Bot* 🎨✨\n\n"
        "📸 Just send me a photo and I will turn it into beautiful Ghibli-style art 😍",
        parse_mode="Markdown")

# Handle photos
@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    file_info = bot.get_file(message.photo[-1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    with open("input.jpg", 'wb') as new_file:
        new_file.write(downloaded_file)

    bot.reply_to(message, "✅ Photo received!\nNext step: Convert to Ghibli Style... (Coming soon)")

# Start polling
bot.polling()
