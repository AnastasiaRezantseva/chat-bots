import urllib.request  # for working with url's (opening and reading)
import os
import json
from dotenv import load_dotenv

load_dotenv()


# ** можем передать любой параметр
def makeRequest(method: str, **param) -> dict:
    json_data = json.dumps(param).encode("utf-8")  # data = {"offset: offset"}

    request = urllib.request.Request(
        method="POST",
        url=f'{os.getenv("TELEGRAM_BASE_URI")}/{method}',  # создание url, getenv - получение токена (переменной окружения)
        data=json_data,
        headers={"Content-Type": "application/json"},
    )

    # urlopen выполняет HTTP запрос
    with urllib.request.urlopen(request) as response:
        response_body = response.read().decode(
            "utf-8"
        )  # with - гарантирует закрытое соединение, read - читает байты, decode - декодирует байты в строку
        response_json = json.loads(response_body)  # преоразует json в dict
        assert response_json["ok"] == True
        return response_json["result"]  # возвращает массив обновлений


# возвращает словарь (в c++ map (key: value))
def getUpdates(offset: int) -> dict:
    return makeRequest("getUpdates", offset=offset)


def sendMessage(chat_id: int, text: str) -> dict:
    return makeRequest("sendMessage", chat_id=chat_id, text=text)


def getMe() -> dict:
    return makeRequest("getMe")
