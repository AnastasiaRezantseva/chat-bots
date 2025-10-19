import bot.telegram_client 
from bot.handler import Handler

class MessageSticker(Handler):
    
    def can_handle(self, update: dict) -> bool:
        return "message" in update and "sticker" in update["message"]


    def handle(self, update: dict) -> bool:
        bot.telegram_client.sendSticker(
                        chat_id=update["message"]["chat"]["id"],
                        sticker=update["message"]["sticker"]["file_id"],
                    )   
        return False    

   
    
