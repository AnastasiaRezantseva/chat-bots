from bot.handlers.handler import Handler
from bot.handlers.database_handler import UpdateDataBase
from bot.handlers.ensure_user_exists import EnsureUserExists
from bot.handlers.message_start import MessageStart
from bot.handlers.pizza_selection import PizzaSelectionHandler
from bot.handlers.pizza_size import PizzaSizeHandler

def get_handlers() -> list[Handler]:
    return[
        UpdateDataBase(),
        EnsureUserExists(),
        MessageStart(),
        PizzaSelectionHandler(),
        PizzaSizeHandler(),
    ]