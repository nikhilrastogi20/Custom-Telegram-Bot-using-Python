from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
  
updater = Updater("5007280440:AAGbY9jMq9ppDvoWcPXvGAUYnDrCv5GgUas", use_context=True)

def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Hello sir,  Welcome to Nikhil's Bot. Please write /help to see the commands available.")
  
def help(update: Update, context: CallbackContext):
    update.message.reply_text("""Available Commands :-
    /date_time - To get the time and date
    /youtube - To get the youtube URL
    /linkedin - To get the LinkedIn profile URL
    /gmail - To get gmail URL
    /flipkart - To get flipkart URL
    /amazon - To get amazon URL
    /facebook - To get facebook URL
    /myntra - To get myntra URL
    /google - To get google URL""")
  
  
  def date_time_url(update: Update, context: CallbackContext):
    update.message.reply_text("https://www.timeanddate.com/worldclock/india/new-delhi")

  
  def gmail_url(update: Update, context: CallbackContext):
    update.message.reply_text(" Gmail Link =>  https://www.google.com/gmail/")
   
  
  
def youtube_url(update: Update, context: CallbackContext):
    update.message.reply_text("Youtube Link =>https://www.youtube.com/")

  
def linkedIn_url(update: Update, context: CallbackContext):
    update.message.reply_text("LinkedIn Link => https://www.linkedin.com/")
  
  
def flipkart_url(update: Update, context: CallbackContext):
    update.message.reply_text(" Flipkart Link =>  https://www.flipkart.com/")


def google_url(update: Update, context: CallbackContext):
    update.message.reply_text(" Google Link =>  https://www.google.com/")  
  
def facebook_url(update: Update, context: CallbackContext):
    update.message.reply_text(" Facebook Link =>  https://www.facebook.com/")


def myntra_url(update: Update, context: CallbackContext):
    update.message.reply_text(" Myntra Link =>  https://www.myntra.com/")


def amazon_url(update: Update, context: CallbackContext):
    update.message.reply_text(" Amazon Link =>  https://www.amazon.com/")

def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry '%s' is not a valid command" % update.message.text)
  
  
def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry I can't recognize you , you said '%s'" % update.message.text)
  
  
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('date_time', date_time_url))
updater.dispatcher.add_handler(CommandHandler('youtube', youtube_url))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('linkedin', linkedIn_url))
updater.dispatcher.add_handler(CommandHandler('gmail', gmail_url))
updater.dispatcher.add_handler(CommandHandler('flipkart', flipkart_url))
updater.dispatcher.add_handler(CommandHandler('amazon', amazon_url))
updater.dispatcher.add_handler(CommandHandler('myntra', myntra_url))
updater.dispatcher.add_handler(CommandHandler('facebook', facebook_url))
updater.dispatcher.add_handler(CommandHandler('google', google_url))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))  # Filters out unknown commands
  
# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))
  
updater.start_polling()
