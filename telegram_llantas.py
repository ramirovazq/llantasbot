#!/usr/bin/env python
# pylint: disable=C0116,W0613
# This program is dedicated to the public domain under the CC0 license.

"""
First, a few callback functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Example of a bot-user conversation using ConversationHandler.
Send /start to initiate the conversation.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging, os
# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
)

from utils.constants import BRAND_OPTIONS_AS_LIST
from utils.constants import STATUS_OPTIONS_AS_LIST
from utils.constants import OWNERS_OPTIONS_AS_LIST
from utils.constants import MEASURES_OPTIONS_AS_LIST
from utils.constants import ECONOMICO_OPTIONS_AS_LIST
from utils.constants import CANCEL_TEXT

from utils.regexpessions import ALL_BRANDS_REGEX
from utils.regexpessions import ALL_MEASURES_REGEX
from utils.regexpessions import DOTS_REGEX
from utils.regexpessions import ALL_OWNERS_REGEX
from utils.regexpessions import ALL_STATUS_REGEX
from utils.regexpessions import ALL_ECONOMICO_REGEX

from utils.comfortable import open_new_pickle
from utils.comfortable import open_and_save_pickle
from utils.comfortable import read_pickle

QUANTITY, STATUS, BRAND, MEASURE, DOTS, OWNER, ECONOMICO, COMMENT, PHOTO = range(9)

def start(update: Update, context: CallbackContext) -> int:
    """Starts the conversation and asks the user about their gender."""
    user = update.message.from_user
    username = user.first_name

    open_new_pickle(username, "step 0 in pickle")

    logger.info("---- START ---")
    logger.info("User: %s", user.first_name)
    logger.info("---- ASK FOR QUANTITY ---")
    update.message.reply_text(
        'Hola, soy el Bot del almacén de entrega de llantas.\n' +
        CANCEL_TEXT + '¿Cuantas llantas del mismo tipo son?'
    )
    return QUANTITY

def status(update: Update, context: CallbackContext) -> int:
    """Starts the conversation and asks the user about brand."""
    user = update.message.from_user
    username = user.first_name

    open_and_save_pickle(username, "step 2", "quantity", update.message.text)
    logger.info("User %s: quantity %s", user.first_name, update.message.text)
    logger.info("---- ASK FOR STATUS ---")
    update.message.reply_text(
        'Selecciona la status de la llanta.' + 
        CANCEL_TEXT + STATUS_OPTIONS_AS_LIST
    )
    return STATUS

def brand(update: Update, context: CallbackContext) -> int:
    """Starts the conversation and asks the user about brand."""
    user = update.message.from_user
    username = user.first_name

    open_and_save_pickle(username, "step 3", "status", update.message.text)
    logger.info("User %s: status %s", user.first_name, update.message.text)
    logger.info("---- ASK FOR BRAND ---")
    update.message.reply_text(
        'Selecciona la marca de la llanta.\n' + 
        CANCEL_TEXT + BRAND_OPTIONS_AS_LIST
    )
    return BRAND

def measure(update: Update, context: CallbackContext) -> int:
    """Starts the conversation and asks the user about brand."""
    user = update.message.from_user
    username = user.first_name

    open_and_save_pickle(username, "step 4", "brand", update.message.text)
    logger.info("User %s: brand %s", user.first_name, update.message.text)
    logger.info("---- ASK FOR MEASURE ---")
    update.message.reply_text(
        'Selecciona la medida de la llanta.' + 
        CANCEL_TEXT + MEASURES_OPTIONS_AS_LIST
    )
    return MEASURE

def dots(update: Update, context: CallbackContext) -> int:
    """Starts the conversation and asks the user about brand."""
    user = update.message.from_user
    username = user.first_name

    open_and_save_pickle(username, "step 5", "measure", update.message.text)
    logger.info("User %s: measure %s", user.first_name, update.message.text)
    logger.info("---- ASK FOR DOT OR DOTS ---")
    update.message.reply_text(
        'Escribe el DOT empezando con # y 4 digitos.\n'
        'Ejemplo #0521\n'
        'Para mas de un DOT separa por comas\n'
        'No dejes espacio entre los dots:\n'
        'Ejemplo: #0521,#0419,#2334\n' +
        CANCEL_TEXT + 
        'Recuerda que el DOT son 4 digitos'
    )
    return DOTS

def owner(update: Update, context: CallbackContext) -> int:
    """Starts the conversation and asks the user about brand."""
    user = update.message.from_user
    username = user.first_name

    open_and_save_pickle(username, "step 6", "dots", update.message.text)
    logger.info("User %s: dots %s", user.first_name, update.message.text)
    logger.info("---- ASK FOR OWNER ---")
    update.message.reply_text(
        'Selecciona al permisionario de la llanta.' + 
        CANCEL_TEXT + OWNERS_OPTIONS_AS_LIST
    )
    return OWNER

def economico(update: Update, context: CallbackContext) -> int:
    """Starts the conversation and asks the user about brand."""
    user = update.message.from_user
    username = user.first_name

    open_and_save_pickle(username, "step 7", "owner", update.message.text)
    logger.info("User %s: owner %s", user.first_name, update.message.text)
    logger.info("---- ASK FOR ECONOMICO ---")
    update.message.reply_text(
        'Selecciona el economico al que va la llanta.' + 
        CANCEL_TEXT + ECONOMICO_OPTIONS_AS_LIST
    )
    return ECONOMICO

def comment(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    username = user.first_name

    open_and_save_pickle(username, "step 8", "economico", update.message.text)
    logger.info("User %s: economico %s", user.first_name, update.message.text)
    logger.info("---- ASK FOR COMMENT ---")
    update.message.reply_text(
        'Agrega un comentario a la entrega de la llanta.\n' 
        'Ejemplo: Entrega maestro talachero \n'+ 
        CANCEL_TEXT
    )
   
    return COMMENT

def photo(update: Update, context: CallbackContext) -> int:
    """Stores the photo and asks for a location."""
    user = update.message.from_user
    username = user.first_name

    open_and_save_pickle(username, "step 9", "comment", update.message.text)
    logger.info("User %s: comment %s", user.first_name, update.message.text)
    logger.info("---- ASK FOR PHOTO ---")

    update.message.reply_text(
        'Envia una foto de la(s) llanta(s), ó '
        'selecciona /skip si no vas a enviar una foto.',
        reply_markup=ReplyKeyboardRemove(),
    )
    return PHOTO

def skip_photo(update: Update, context: CallbackContext) -> int:
    """Skips the photo and asks for a location."""
    user = update.message.from_user
    username = user.first_name

    open_and_save_pickle(username, "step 10", "photo", "")
    logger.info("User %s: owner %s", user.first_name, update.message.text)
    logger.info("---- ASK FOR PHOTO ---")
    update.message.reply_text('No se envió foto. Llantas guardadas.¡Gracias!')

    return PHOTO

def goodbye_with_photo(update: Update, context: CallbackContext) -> int:
    
    user = update.message.from_user
    username = user.first_name
    logger.info("USER %s: LAST_MESSAGE: %s", user.first_name, update.message.text)

    photo_file = update.message.photo[-1].get_file()
    logger.info("photo_file --->")
    logger.info(photo_file)
    open_and_save_pickle(username, "step 10", "photo", "photo_file.jpg")
    photo_file.download('user_photo.jpg')
    logger.info("Photo of %s: %s", user.first_name, photo_file)

    dict_result = read_pickle(username, "final_step")
    logger.info(dict_result)
    update.message.reply_text('Llantas guardadas.!Gracias!')
    return ConversationHandler.END

def goodbye(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    username = user.first_name

    logger.info("USER %s: LAST_MESSAGE: %s", user.first_name, update.message.text)

    dict_result = read_pickle(username, "final_step")
    logger.info(dict_result)
    update.message.reply_text('Gracias! Llantas guardadas.')
    logger.info("---- END ---")
    return ConversationHandler.END

def cancel(update: Update, context: CallbackContext) -> int:
    """Cancels and ends the conversation."""
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text(
        'Adiós! Espero poder hablar contigo despues.', reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END

def help(update, context):
    logger.info("Command: Help")

    ayuda_text = "opciones: "
    commands_list = [
        "/entrega", 
        "/cancelar",
        "/help",
    ]
    ayuda_text = ayuda_text + " ".join(commands_list)

    update.message.reply_text("Ayuda")
    context.bot.send_message(chat_id=update.effective_chat.id, text=ayuda_text)

def unknown(update, context):
    logger.info("Unknown command handler")
    context.bot.send_message(chat_id=update.effective_chat.id, text="No te entiendo lo que solicitas. /help")

def main() -> None:
    """Run the bot."""
    TOKEN_FATHER = os.getenv("TOKEN_FATHER")
    # Create the Updater and pass it your bot's token.
    updater = Updater(TOKEN_FATHER)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Add conversation handler with the states GENDER, PHOTO, LOCATION and BIO
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('entrega', start)],
        states={
            QUANTITY: [MessageHandler(Filters.regex('^([\s\d]+)$'), status)],
            STATUS: [MessageHandler(Filters.regex(ALL_STATUS_REGEX), brand)],
            BRAND: [MessageHandler(Filters.regex(ALL_BRANDS_REGEX), measure)],
            MEASURE: [MessageHandler(Filters.regex(ALL_MEASURES_REGEX), dots)],
            DOTS: [MessageHandler(Filters.regex(DOTS_REGEX), owner)],
            OWNER: [MessageHandler(Filters.regex(ALL_OWNERS_REGEX), economico)],
            ECONOMICO: [MessageHandler(Filters.regex(ALL_ECONOMICO_REGEX), comment)],
            COMMENT: [MessageHandler(Filters.text & ~Filters.command, photo), CommandHandler('skip', photo)],
            PHOTO: [MessageHandler(Filters.photo, goodbye_with_photo), CommandHandler('skip', goodbye)],
        },
        fallbacks=[CommandHandler('cancelar', cancel)],
    )

    dispatcher.add_handler(conv_handler)

    # add help command
    help_command = MessageHandler(Filters.command, help)
    dispatcher.add_handler(help_command)

    # add unknown handler
    unknown_handler = MessageHandler(Filters.command, unknown)
    dispatcher.add_handler(unknown_handler)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()