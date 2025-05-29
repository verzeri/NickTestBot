import logging
import random
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

# Configurazione logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Lista di barzellette
barzellette = [
    "Qual è il colmo per un giardiniere? Piantare in asso la fidanzata!",
    "Due cannibali stanno mangiando un clown. Uno dice all'altro: 'Secondo te sa di divertente?'",
    "Perché i libri di matematica sono sempre tristi? Perché hanno troppi problemi.",
    "Cosa fa un'ape nel deserto? Un apericolo!",
    "Cosa dice un uccello quando sbatte contro un vetro? Vetro o falso?",
    "Qual è il cane più veloce del mondo? Il bassotto perché è aerodinamico!",
    "Cosa dice zero a otto? Bel cinturone!",
    "Che cosa hanno in comune un elefante e una fragola? Entrambi sono rossi, tranne l'elefante.",
    "Qual è il colmo per un elettricista? Restare scioccato!",
    "Perché l'informatico non esce mai di casa? Perché ha perso la connessione!"
]

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Ciao {update.effective_user.first_name}! Sono il bot delle barzellette.\nUsa /barzelletta per farti raccontare una barzelletta!')

# Comando /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Comandi disponibili:\n/start - Inizia a usare il bot\n/barzelletta - Racconta una barzelletta casuale')

# Comando /barzelletta
async def barzelletta(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Scegli una barzelletta casuale
    barzelletta_casuale = random.choice(barzellette)
    await update.message.reply_text(barzelletta_casuale)

# Risposta ai messaggi normali
async def risposta_normale(update: Update, context: ContextTypes.DEFAULT_TYPE):
    messaggio = update.message.text.lower()
    if "barzelletta" in messaggio:
        # Se l'utente chiede una barzelletta in un messaggio normale
        await barzelletta(update, context)
    else:
        await update.message.reply_text('Vuoi sentire una barzelletta? Usa il comando /barzelletta!')

def main():
    # Ottieni il token dalla variabile d'ambiente
    token = os.environ.get('8130808308:AAHBXTliHWQ40c8TV8pqpZCqgIbuOLGYaTU')
    if not token:
        raise ValueError("Nessun token Telegram trovato. Imposta la variabile d'ambiente TELEGRAM_TOKEN.")
    
    application = ApplicationBuilder().token(token).build()
    
    # Aggiungi i gestori dei comandi
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("barzelletta", barzelletta))
    
    # Gestore per i messaggi normali
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, risposta_normale))
    
    # Avvia il bot
    print("Bot delle barzellette avviato!")
    application.run_polling()

if __name__ == '__main__':
    main()