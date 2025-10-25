from bot.dispatcher import Dispatcher
import bot.telegram_client
import time

def start_long_polling(dispatcher: Dispatcher) -> None:
    next_update_offset = 0
    while True:
            updates = bot.telegram_client.getUpdates(offset=next_update_offset)         
            for update in updates:
                next_update_offset = max(next_update_offset, update["update_id"] + 1)
                dispatcher.dispatch(update)
                print(".", end="", flush=True)
            time.sleep(1)