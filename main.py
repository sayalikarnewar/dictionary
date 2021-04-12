from aiohttp import web
import jinja2
import aiohttp_jinja2
from routes import routes


app = web.Application()
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('templates'))

routes(app)

web.run_app(app)