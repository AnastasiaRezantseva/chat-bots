import  bot.database_client
from bot.handlers.handler import Handler, HandlerStatus

class EnsureUserExists:
    def can_handle(self, update: dict, state: str, order_json: dict) -> bool:
        return "message" in update and "from" in update["message"]

    def handle(self, update: dict, state: str, order_json: dict) -> HandlerStatus:
        telegram_id = update["message"]["from"]["id"]
        bot.database_client.ensure_user_exists(telegram_id)
        return HandlerStatus.CONTINUE