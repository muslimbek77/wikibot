from asyncore import dispatcher
from telegram import Update
from telegram.bot import Bot
from telegram.user import User
import settings
from telegram.ext import Updater,Dispatcher,CommandHandler,CallbackContext


bot =Bot(token=settings.TELEGRAM_TOKEN)

updater=Updater(token=settings.TELEGRAM_TOKEN)

def start(update:Update,context:CallbackContext):
    update.message.reply_text("salom")
    context.bot.send_message(chat_id=update.message.chat_id,text='yana bir bor salom')

dispatcher=updater.dispatcher
dispatcher.add_handler(CommandHandler('start',start))

updater.start_polling()
updater.idle()


# print(bot.get_me())

# user:User=bot.get_me()

# print(user.link)