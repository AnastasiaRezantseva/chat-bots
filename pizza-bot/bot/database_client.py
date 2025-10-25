import sqlite3
import os
import json
from dotenv import load_dotenv

load_dotenv()


def recreate_database() -> None:
    connection = sqlite3.connect(os.getenv("SQLITE_DATABASE_PATH"))
    with connection:
        connection.execute("DROP TABLE IF EXISTS telegram_updates")
        connection.execute(
            """
                           CREATE TABLE IF NOT EXISTS telegram_updates
                            (
                                id INTEGER PRIMARY KEY,
                                payload TEXT NOT NULL
                            )

                        """
        )
        connection.execute(
            """
                           CREATE TABLE IF NOT EXISTS users
                            (
                                id INTEGER PRIMARY KEY,
                                telegram_id INTEGER NOT NULL UNIQUE,
                                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                                state TEXT DEFAULT NULL,
                                order_json TEXT DEFAULT NULL
                            )

                        """
        )
    connection.close()


def persist_updates(updates: list) -> None:
    connection = sqlite3.connect(os.getenv("SQLITE_DATABASE_PATH"))
    with connection:
        data = []
        for update in updates:
            data.append((json.dumps(update, ensure_ascii=False, indent = 2),))

        connection.executemany(
            "INSERT INTO telegram_updates (payload) VALUES (?)",
            data,
        )
    connection.close()

def ensure_user_exists(telegram_id: int) -> None:
    """Ensure a user with the given telegram_id exists in the users table.
    If the user doesn't exist, create them. All operations happen in a single transaction."""
    with sqlite3.connect(os.getenv("SQLITE_DATABASE_PATH")) as connection:
        with connection:
            cursor = connection.execute(
                "SELECT 1 FROM users WHERE telegram_id = ?", (telegram_id,))
            
            if cursor.fetchone() is None:
                connection.execute(
                    "INSERT INTO users (telegram_id) VALUES (?)", (telegram_id,))


def update_user_state(telegram_id: int, state: str) -> None:
    """Update user state in the users table."""
    with sqlite3.connect(os.getenv("SQLITE_DATABASE_PATH")) as connection:
        with connection:
            connection.execute(
                "UPDATE users SET state = ? WHERE telegram_id = ?",
                (state, telegram_id)
            )


def clear_user_state_and_order(telegram_id: int) -> None:
    """Clear user state and order in the users table."""
    with sqlite3.connect(os.getenv("SQLITE_DATABASE_PATH")) as connection:
        with connection:
            connection.execute(
                "UPDATE users SET state = NULL, order_json = NULL WHERE telegram_id = ?",
                (telegram_id,)
            )

def get_user(telegram_id: int) -> dict:
    with sqlite3.connect(os.getenv("SQLITE_DATABASE_PATH")) as connection:
        with connection:
            cursor = connection.execute(
                "SELECT id, telegram_id, created_at, state, order_json FROM users WHERE telegram_id = ?", (telegram_id,)
            )
            result = cursor.fetchone()
            if result:
                return {
                    'id': result[0],
                    'telegram_id': result[1],
                    'created_at': result[2],
                    'state': result[3],
                    'order_json': result[4]
                }
            return None
