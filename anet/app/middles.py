import json
import traceback

from aiohttp import web, web_exceptions
from tortoise.exceptions import DoesNotExist, IntegrityError


@web.middleware
async def check_data(request, handler):
    try:
        await request.json()
    except json.decoder.JSONDecodeError:
        return web.json_response(
            {"message": "Invalid data. {}".format(await request.text())}, status=400
        )
    except web_exceptions.HTTPRequestEntityTooLarge as err:
        traceback.print_exc()
        return web.json_response({"message": str(err)}, status=400)
    return await handler(request)


@web.middleware
async def check_info(request, handler):
    try:
        return await handler(request)
    except (KeyError, IOError) as err:
        return web.json_response({"messsage": str(err)}, status=400)
    except DoesNotExist as error:
        return web.json_response({"message": str(error)}, status=404)
    except IntegrityError as err:
        return web.json_response({"message": "Already exists"}, status=400)
