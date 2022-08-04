import os
import logging
import responses
from telegram.ext import *
from dotenv import load_dotenv

# we use this to get api key from env files
load_dotenv()
API_KEY = os.getenv('API_KEY')

# Set up the logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info('Starting Bot...')


# We defined this fuction to use as commands
# all update.message are reply from bots to user

def yardim(update, context):
    update.message.reply_text('Type cmd for options or click /cmd')


def iletisim(update, context):
    update.message.reply_text(
'Bize Ulaşın\n 📞 +905306480734\n\n <a href="http://wa.me/905411954888">📩 WhatsApp hattımız</a>\n\n mzndanismanlik@gmail.com\n Nef 22 Ataköy/İstanbul', disable_web_page_preview=True, parse_mode="HTML")


def danismanlik(update, context):
    update.message.reply_text(
 'Danışmanlığımızda:\n ■ Hesap açılışı yapılıyor. (şirketli veya şirketsiz)\n ■ 15 farklı ürün analiz yöntemi öğretiliyor.\n ■ Yazılım kullanımı öğretiliyor.\n ■ Seller Central kullanımı öğretiliyor.\n ■ Hesap sağlığı ve Suspend türleri öğretiliyor.\n ■ Suspend olmamak için taktikler öğretiliyor.\n ■ Yazılım ve Seller Central ayarları yapılıyor.\n ■ Ürün yüklenmesi ve gönderimi öğretiliyor.\n ■ Müşteri ilişkileri ve iade yöntemi öğretiliyor.\n ■ <b>Büyük Dropshippingcilerin bazı ileri taktikleri anlatılıyor</b>\n ■ Feedback alma yolları (garantili) öğretiliyor.\n ■ Buybox alma ayarı yapılıyor. (%80 çalışıyor)', parse_mode="HTML")


def list(update, context):
    update.message.reply_text(
        'All commands you can use\n /help : offcourse for help dumbo\n\n /notes: To get notes\n\n /projects : for all projects🔥')

# there two methods to crete functions to get repond from bot this is 2nd one


def socials(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="List of Socails are down below:\n {Github} https://github.com/amrohan\n\n {Twitter} https://twitter.com/amrohann\n\n {Instagram} https://www.instagram.com/amrohann\n\n {Email} hello@rohan.ml")


def source_code(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="the source code can be accessed here\n {Github}\n https://github.com/amrohan/ChatBot")


def projects(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="List of projects are down below:\n \n {Chat App} \n https://chathub.gq \n \n { LinkTree } \n https://linkhub.ml")


def handle_message(update, context):
    text = str(update.message.text).lower()
    logging.info(f'User ({update.message.chat.id}) says: {text}')

    # Bot response
    response = responses.get_response(text)
    update.message.reply_text(response)


def error(update, context):
    # Logs errors
    logging.error(f'Update {update} caused error {context.error}')


# Run the programms from here
if __name__ == '__main__':
    updater = Updater(API_KEY, use_context=True)
    dp = updater.dispatcher

    # Commands handler which callback our commands when user ask for it
    dp.add_handler(CommandHandler('yardim', yardim))

    dp.add_handler(CommandHandler('iletisim', iletisim))

    dp.add_handler(CommandHandler('hizmetler', hizmetler))

    dp.add_handler(CommandHandler('danismanlik', danismanlik))

    dp.add_handler(CommandHandler('socials', socials))

    dp.add_handler(CommandHandler('source_code', source_code))

    dp.add_handler(CommandHandler('projects', projects))

    # Messages
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    # Log all errors
    dp.add_error_handler(error)

    # Run the bot
    updater.start_polling(1.0)
    # Idle state give bot time to go in idle
    updater.idle()
