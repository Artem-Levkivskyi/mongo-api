from aiohttp import web
from routes import app
import pytest


async def test_get():
    post_request = await app.post("/car", json={"manufacturer": "Volkswagen", "model": "Golf Plus", "colour": "black", "year": "2018", "vin": "WVWDB4505LK234577"})
    assert post_request.status == 200