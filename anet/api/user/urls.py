from aiohttp import web, web_exceptions
from controller import Controller
from . import views

Controller.add("/account", views.UserView, name="user_view")
# Controller.add("", lambda r: web_exceptions.HTTPFound(Controller.get("user_view").handler, name = "base_user"))
