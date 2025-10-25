from bot.dispatcher import Dispatcher
from bot.handlers import get_handlers
from bot.long_polling import start_long_polling



if __name__ == "__main__":
    try:
        dispatcher = Dispatcher()
        dispatcher.add_handler(*get_handlers()) 
        start_long_polling(dispatcher)
        
    except KeyboardInterrupt:
        print("\nBye!")
