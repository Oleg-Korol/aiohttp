import json

from aiohttp import web

# from tortoise.exceptions import DoesNotExist
from anet.api.user.models import User
from datetime import datetime


class Serializer(json.JSONEncoder):
    def default(self, value):
        if isinstance(value, datetime):
            return value.isoformat()
        return str(value)


class UserView(web.View):
    async def get(self):
        # try:
        data = await self.request.json()
        # except json.decoder.JSONDecoderError:
        #    return web.json_response({"message": "invalid data"}, status=400)
        # try:
        user = await User.get(username=data["username"]).values(
            "id", "username", "email", "created", "status"
        )
        #    return web.json_response({"message": "user not found"}, status=404)
        # except KeyError:
        #    return web.json_response({"message": "invalid   data"}, status=400)
        # return web.json_response({"result": "text"}, status=200)
        return web.json_response(
            {"result": user}, status=200, dumps=lambda v: json.dumps(v, cls=Serializer)
        )

    async def post(self):
        data = await self.request.json()
        new_user = await User.create(**data)
        return web.json_response({"result": f"{new_user.id=}"}, status=200)

    async def put(self):
        data = await self.request.json()
        # data.pop("username")
        if isinstance(data, dict):
            user = await User.filter(username=data.pop("username")).update(**data)
        elif isinstance(data, list):
            u_name = [el["username"] for el in data]
            users = await User.filter(username__in=u_name)
            print(users)

        # user =  await User.all().update(**data)
        return web.json_response({"result": "text"}, status=200)

    async def delete(self):
        data = await self.request.json()
        return web.json_response({"result": "text"}, status=200)
