from telegram import Update, LabeledPrice
from telegram.ext import Application, CommandHandler, PreCheckoutQueryHandler, MessageHandler, filters, ContextTypes
import os

BOT_TOKEN = os.getenv("BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome! Use /buy to CONFIRM BOOKING with Telegram Stars."
    )

# Buy command (sends invoice)
async def buy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_invoice(
        title="CONFIRM YOUR BOOKING",
        description="High-quality GIRLS AVAILABLE",
        payload="image-pack",
        provider_token="",   # must be empty for Stars
        currency="XTR",      # Stars currency
        prices=[LabeledPrice("Image Pack", 50)]  # 50 Stars
    )

# Pre-checkout handler (MUST confirm checkout)
async def precheckout(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.pre_checkout_query
    await query.answer(ok=True)

# Handle successful payment
async def successful_payment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Payment successful! Here’s your product:")
    await update.message.reply_photo(open("image_pack.jpg", "rb"))

# Build the bot application
app = Application.builder().token(BOT_TOKEN).build()

# Add handlers
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("buy", buy))
app.add_handler(PreCheckoutQueryHandler(precheckout))   # ✅ Correct handler
app.add_handler(MessageHandler(filters.SUCCESSFUL_PAYMENT, successful_payment))

# Run the bot
app.run_polling()
