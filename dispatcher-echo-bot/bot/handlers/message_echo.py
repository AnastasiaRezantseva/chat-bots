from bot.handler import Handler
import bot.telegram_client


class MessageEcho(Handler):
    def can_handle(self, update: dict) -> bool:
        return "message" in update and "text" in update["message"]

    def handle(self, update: dict) -> bool:
        bot.telegram_client.sendMessage(
            chat_id=update["message"]["chat"]["id"],
            text=update["message"]["text"],
        )
        return False
