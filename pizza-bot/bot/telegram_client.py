import urllib.request  # for working with url's (opening and reading)
import os
import json
from dotenv import load_dotenv

load_dotenv()

def makeRequest(method: str, **param) -> dict:
    json_data = json.dumps(param).encode("utf-8")

    request = urllib.request.Request(
        method="POST",
        url=f'{os.getenv("TELEGRAM_BASE_URI")}/{method}',
        data=json_data,
        headers={"Content-Type": "application/json"},
    )

    # urlopen выполняет HTTP запрос
    with urllib.request.urlopen(request) as response:
        response_body = response.read().decode(
            "utf-8"
        )
        response_json = json.loads(response_body)
        assert response_json["ok"] == True
        return response_json["result"]  


def getUpdates(**params) -> dict:
    return makeRequest("getUpdates", **params)


def sendMessage(chat_id: int, text: str, **params) -> dict:
    return makeRequest("sendMessage", chat_id=chat_id, text=text, **params)

def getMe() -> dict:
    return makeRequest("getMe")

def answerCallbackQuery(callback_query_id: str, **params) -> dict:
    return makeRequest("answerCallbackQuery", callback_query_id=callback_query_id, **params)

def deleteMessage(chat_id: int,message_id : int, **params) -> dict:
    return makeRequest("deleteMessage", chat_id=chat_id,message_id=message_id, **params)
