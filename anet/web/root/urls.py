from controller import Controller
from anet.settings import API_V

Controller.include("", "anet.web.home.urls")

Controller.include(f"/api/v_{API_V}", "anet.api.root.urls")
