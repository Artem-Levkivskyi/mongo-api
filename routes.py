from api import mongodb_api
from views import taskbar
from aiohttp import web
import aiohttp_jinja2
import logging
import asyncio
import jinja2


logging.basicConfig(level=logging.INFO)


@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)

    # Taskbar URL view
    app.router.add_route('GET', '/car', taskbar.web_render)

    # Static files
    app['static_root_url'] = '/static'
    app.router.add_static('/static', 'static', name='static')

    # REST API endpoints handlers
    app.router.add_post('/car', mongodb_api.create)
    app.router.add_get('/car', mongodb_api.get_single)
    app.router.add_delete('/car', mongodb_api.delete)
    app.router.add_put('/car', mongodb_api.update)

    # Server starting
    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('./'))
    server = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9090)
    logging.info('server started at http://127.0.0.1:9090')

    return server


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass
