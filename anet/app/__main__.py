from aiohttp import web
from .srv import create_app


try:
    web.run_app(create_app(), host="127.0.0.1", port=8080)
except KeyboardInterrupt:
    print("\rStop ANET")
