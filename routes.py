from aiohttp import web
from api import mongodb_api

app = web.Application()

# API routers
app.router.add_post('/car', mongodb_api.create)
app.router.add_get('/car', mongodb_api.get_single)
app.router.add_delete('/car', mongodb_api.delete)
app.router.add_put('/car', mongodb_api.update)


web.run_app(app)
