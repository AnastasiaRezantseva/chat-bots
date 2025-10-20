from bot.dispatcher import Dispatcher
from bot.handlers.message_echo import MessageEcho
from bot.long_polling import start_long_polling
from bot.handlers.database_handler import UpdateDataBase
from bot.handlers.message_photo import MessagePhoto
from bot.handlers.message_sticker import MessageSticker


if __name__ == "__main__":
    try:
        dispatcher = Dispatcher()
        dispatcher.add_handler(UpdateDataBase()) 
        dispatcher.add_handler(MessageEcho())
        dispatcher.add_handler(MessagePhoto())
        dispatcher.add_handler(MessageSticker())
        start_long_polling(dispatcher)
        
    except KeyboardInterrupt:
        print("\nBye!")
