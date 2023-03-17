import os
import pathlib

__all__ = ("BASE_DIR", "DB_CONFIG", "API_V")

BASE_DIR = pathlib.Path(__file__).parent.parent.absolute()

DB_CONFIG = {
    "connections": {
        # "default": {
        #     "engine": "tortoise.backends.asyncpg",
        #     "credentials": {
        #        "host": os.getenv("PG_HOST"),
        #        "port": int(os.getenv("PG_PORT")),
        #        "user": "a_net",
        #        "password": "qwerty123",
        #        "database": "anet",
        #                    },
        "default": f"sqlite://{BASE_DIR / 'db.sqlite'}"
    },
    "apps": {
        "user": {
            "models": ["anet.api.user.models"],
            "default_connection": "default",
        }
    },
    "use_tz": True,
    "timezone": "UTC",
}

API_V = "1.0"
