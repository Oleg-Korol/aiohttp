import jinja2
from aiohttp import web
from aiohttp_jinja2 import setup as jinja_setup
from controller import controller_setup
from tortoise.contrib.aiohttp import register_tortoise
from anet import settings
from .middles import check_data, check_info


# method for development
def create_app():
    """Creates in instance of the application and configures it for further launch"""
    app = web.Application(middlewares=(check_data, check_info))
    jinja_setup(
        app,
        loader=jinja2.FileSystemLoader(
            [
                path / "templates"
                for path in (settings.BASE_DIR / "web").iterdir()
                if path.is_dir() and (path / "templates").exists()
            ]
        ),
    )
    controller_setup(app, root_urls="anet.web.root.urls")
    register_tortoise(app, config=settings.DB_CONFIG, generate_schemas=True)
    # app.router.add_route("GET", "/", HomePage, name="home_page")
    return app


# method for production(To run in context "Gunicorn")
async def get_app():
    return create_app()
