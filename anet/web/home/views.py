from aiohttp import web
from aiohttp_jinja2 import template


class HomePage(web.View):
    @template("home.html")
    async def get(self):
        print(self.request.headers)
        return {"key": "Info"}
