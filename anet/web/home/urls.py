from controller import Controller
from .views import HomePage


Controller.add("", HomePage, name="home_page")
