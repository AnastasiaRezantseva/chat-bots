from typing import List, Dict, Any

def build_inline_keyboard(buttons: List[Dict[str, str]]) -> Dict[str, Any]:
    return {"inline_keyboard": [[btn] for btn in buttons]}

def pizza_keyboard() -> dict:
    return{
        "inline_keyboard": [
                        [
                            {"text": "Margherita", "callback_data": "pizza_margherita"},
                            {"text": "Pepperoni", "callback_data": "pizza_pepperoni"},
                        ],
                        [
                            {
                                "text": "Quattro Stagioni",
                                "callback_data": "pizza_quattro_stagioni",
                            },
                            {
                                "text": "Capricciosa",
                                "callback_data": "pizza_capricciosa",
                            },
                        ],
                        [
                            {"text": "Diavola", "callback_data": "pizza_diavola"},
                            {"text": "Prosciutto", "callback_data": "pizza_prosciutto"},
                        ],
                    ],
    }

def size_keyboard() -> dict:
    return {
        "inline_keyboard": [
                        [
                            {"text": "Small (25cm)", "callback_data": "size_small"},
                            {"text": "Medium (30cm)", "callback_data": "size_medium"},
                        ],
                        [
                            {"text": "Large (35cm)", "callback_data": "size_large"},
                            {"text": "Extra Large (40cm)", "callback_data": "size_xl"},
                        ],
                    ],
    }

def drinks_keyboard() -> dict:
    return {
        "inline_keyboard": [
                        [
                            {"text": "Coca-Cola", "callback_data": "drink_coca_cola"},
                            {"text": "Pepsi", "callback_data": "drink_pepsi"},
                        ],
                        [
                            {
                                "text": "Orange Juice",
                                "callback_data": "drink_orange_juice",
                            },
                            {
                                "text": "Apple Juice",
                                "callback_data": "drink_apple_juice",
                            },
                        ],
                        [
                            {"text": "Water", "callback_data": "drink_water"},
                            {"text": "Iced Tea", "callback_data": "drink_iced_tea"},
                        ],
                        [
                            {"text": "No drinks", "callback_data": "drink_none"},
                        ],
                    ],
    }