from telegram import Update, LabeledPrice
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import os

# Load your bot token (set BOT_TOKEN in hosting dashboard or replace with string for local testing)
BOT_TOKEN = os.getenv("BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome! Use /buy to purchase digital products with Telegram Stars."
    )

# Buy command (sends invoice)
async def buy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_invoice(
        title="Cyberpunk Image Pack",
        description="High-quality glitch art images",
        payload="image-pack",
        provider_token="",   # Leave empty for Stars
        currency="XTR",      # Stars currency
        prices=[LabeledPrice("Image Pack", 100)]  # 100 Stars
    )

# Handle successful payment
async def successful_payment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Payment successful! Here’s your product:")
    # Send your file (replace with your actual file path)
    await update.message.reply_document(open("image_pack.zip", "rb"))

# Build the bot application
app = Application.builder().token(BOT_TOKEN).build()

# Add handlers
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("buy", buy))
app.add_handler(MessageHandler(filters.SUCCESSFUL_PAYMENT, successful_payment))

# Run the bot
app.run_polling()
