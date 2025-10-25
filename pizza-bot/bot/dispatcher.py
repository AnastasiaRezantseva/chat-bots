from bot.handlers.handler import Handler
from bot.database_client import get_user
import json

class Dispatcher:
    def __init__(self):
        self._handlers: list[Handler] = []

    def add_handler(self, *handlers: list[Handler]) -> None:
        for handler in handlers:
            self._handlers.append(handler)

    def _get_telegram_id_from_update(self, update: dict) -> int | None:
        #start button
        if "message" in update:
            return update["message"]["from"]["id"]
        #any other button 
        elif "callback_query" in update:
            return update["callback_query"]["from"]["id"]
        return None
    
    def dispatch(self, update: dict) -> None:

        telegram_id = self._get_telegram_id_from_update(update)
        user = get_user(telegram_id) if telegram_id else None

        user_state = user.get("state") if user else None

        order_json = user["order_json"] if user else "{}"
        if order_json is None:
            order_json = "{}"
        order_json = json.loads(order_json)


        for handler in self._handlers:
            if handler.can_handle(update, user_state, order_json):
                signal = handler.handle(update, user_state, order_json)
                if not signal:
                    break