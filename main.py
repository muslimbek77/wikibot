from asyncore import dispatcher
from telegram import Update
from telegram.bot import Bot
from telegram.user import User
import settings
from telegram.ext import Updater,Dispatcher,CommandHandler,CallbackContext
import requests


bot =Bot(token=settings.TELEGRAM_TOKEN)

updater=Updater(token=settings.TELEGRAM_TOKEN)

def start(update:Update,context:CallbackContext):
    update.message.reply_text("salom")
    context.bot.send_message(chat_id=update.message.chat_id,text='yana bir bor salom')
def search(update:Update,context:CallbackContext):
    args=context.args
    search_text=' '.join(args)
    response=requests.get('https://en.wikipedia.org/w/api.php',{
        'action':'opensearch',
        'search': search_text,
        'limit':1,
        'namespace':0,
        'format':'json',
    })
    result=response.json()
    if len(args)==0:        
        update.message.reply_text("Hech bo'lmasa nimadir kiriting")


    elif len(result[3]):
        update.message.reply_text("sizning so'rovvingiz bo'yicha havola "+ result[3][0])
    else:
        update.message.reply_text("sizning so'rovvingiz bo'yicha hech nima topilmadi")
    

dispatcher=updater.dispatcher
dispatcher.add_handler(CommandHandler('start',start))
dispatcher.add_handler(CommandHandler('search',search))


updater.start_polling()
updater.idle()


# print(bot.get_me())

# user:User=bot.get_me()

# print(user.link)