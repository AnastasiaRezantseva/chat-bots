import sqlite3
import os
import json
from dotenv import load_dotenv

load_dotenv()

# храним все обновления
def recreate_database() -> None:
    connection = sqlite3.connect(os.getenv("SQLITE_DATABASE_PATH"))
    with connection:
        connection.execute("DROP TABLE IF EXISTS telegram_events")
        connection.execute(
            """
                           CREATE TABLE IF NOT EXISTS telegram_events
                            (
                                id INTEGER PRIMARY KEY,
                                payload TEXT NOT NULL
                            )

                        """
        )
    connection.close()


def persist_updates(updates: list) -> None:
    connection = sqlite3.connect(os.getenv("SQLITE_DATABASE_PATH"))
    with connection:
        data = []
        for update in updates:
            data.append((json.dumps(update, ensure_ascii=False),))

        connection.executemany(
            "INSERT INTO telegram_events (payload) VALUES (?)",
            data,
        )
    connection.close()
