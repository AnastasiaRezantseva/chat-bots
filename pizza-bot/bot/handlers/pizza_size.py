import json

import bot.telegram_client
import bot.database_client
from bot.handlers.handler import Handler, HandlerStatus
from bot.keyboards.order_keyboards import drinks_keyboard


class PizzaSizeHandler(Handler):
    def can_handle(self, update: dict, state: str, data: dict) -> bool:
        if "callback_query" not in update:
            return False

        if state != "WAIT_FOR_PIZZA_SIZE":
            return False

        callback_data = update["callback_query"]["data"]
        return callback_data.startswith("size_")

    def handle(self, update: dict, state: str, data: dict) -> HandlerStatus:
        telegram_id = update["callback_query"]["from"]["id"]
        callback_data = update["callback_query"]["data"]

        size_mapping = {
            "size_small": "Small (25cm)",
            "size_medium": "Medium (30cm)",
            "size_large": "Large (35cm)",
            "size_xl": "Extra Large (40cm)",
        }

        pizza_size = size_mapping.get(callback_data)
        data["pizza_size"] = pizza_size
        bot.database_client.update_user_order_json(telegram_id, data)
        bot.database_client.update_user_state(telegram_id, "WAIT_FOR_DRINKS")

        bot.telegram_client.answerCallbackQuery(update["callback_query"]["id"])

        bot.telegram_client.deleteMessage(
            chat_id=update["callback_query"]["message"]["chat"]["id"],
            message_id=update["callback_query"]["message"]["message_id"],
        )

        bot.telegram_client.sendMessage(
            chat_id=update["callback_query"]["message"]["chat"]["id"],
            text="Please choose some drinks",
            reply_markup=drinks_keyboard(),
        )
        return HandlerStatus.STOP