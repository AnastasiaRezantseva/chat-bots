import bot.telegram_client 
from bot.handler import Handler

class MessagePhoto(Handler):
    
    def can_handle(self, update: dict) -> bool:
        return "message" in update and "photo" in update["message"]


    def handle(self, update: dict) -> bool:
        bot.telegram_client.sendPhoto(
                        chat_id=update["message"]["chat"]["id"],
                        photo=update["message"]["photo"][-1]["file_id"], # -1   - отправим фото лучшего качества
                    )
        return False    

   
    
