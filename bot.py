import os
import asyncio
from telegram.ext import ApplicationBuilder, MessageHandler, filters

async def bienvenida(update, context):
    await update.message.reply_text(
    "Hola bebe como estas💦🥴\n\n"
    "Te ofrezco:\n"
    "💙 Rica videollamada\n"
    "💙 Sexting\n"
    "💙 Pack de fotos y videos\n"
    "💙 Dick rate\n"
    "💙 Videos personalizados\n"
    "💙 Suscripción canal premium\n\n"
    "Manejo:\n"
    "❤️ Remitly\n"
    "❤️ Bizum\n"
    "❤️ Criptomonedas\n"
    "❤️ BINANCE\n"
    "❤️ Transferencias mexicanas\n"
    "❤️ Transferencias colombianas\n"
    "❤️ Transferencias chilenas\n\n"
    "¿De dónde eres? ¿Y qué te interesa?\n\n"
    "SI NO TIENE DINERO NO ME HABLE.\n"
    "NO HAGO NADA PRESENCIAL, NO PIERDA EL TIEMPO PREGUNTÁNDOMELO."
)
token= os.environ.get("TOKEN")
app = ApplicationBuilder().token(token).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, bienvenida))
app.run_polling()
