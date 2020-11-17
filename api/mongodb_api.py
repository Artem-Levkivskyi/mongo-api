from models.car_model import Car
from mongoengine import errors
from aiohttp import web
import json


async def create(request):

    """ New record creating """

    try:
        print(request)
        response_obj = await Car.create(request.query)

    except KeyError as invalid_key:
        response_obj = {'Status': 'failed', 'Reason': 'undefined key - ' + str(invalid_key)}
        return web.Response(text=json.dumps(response_obj), status=500)

    except errors.NotUniqueError:
        response_obj = {'Status': 'failed', 'Reason': 'vin-code should be an unique parameter'}
        return web.Response(text=json.dumps(response_obj), status=500)

    else:
        return web.Response(text=json.dumps(response_obj), status=200)


async def get_single(request):

    """ Getting single item by some parameters """

    try:
        response_obj = await Car.find(request.query)

    except KeyError as invalid_key:
        response_obj = {'Status': 'failed', 'Reason': 'undefined key - ' + str(invalid_key)}
        return web.Response(text=json.dumps(response_obj), status=500)

    except TypeError:
        response_obj = {'Status': 'failed', 'Reason': 'parameters list are empty'}
        return web.Response(text=json.dumps(response_obj), status=500)

    else:
        return web.Response(text=json.dumps(response_obj), status=200)


async def update(request):

    """ Record updating """

    try:
        response_obj = await Car.update(request.query)

    except KeyError as invalid_key:
        response_obj = {'Status': 'failed', 'Reason': 'undefined key - ' + str(invalid_key)}
        return web.Response(text=json.dumps(response_obj), status=500)

    except TypeError:
        response_obj = {'Status': 'failed', 'Reason': 'parameters list are empty'}
        return web.Response(text=json.dumps(response_obj), status=500)

    else:
        return web.Response(text=json.dumps(response_obj), status=200)


async def delete(request):

    """ Record deleting """

    try:
        response_obj = await Car.drop(request.query)

    except KeyError as invalid_key:
        response_obj = {'Status': 'failed', 'Reason': 'undefined key - ' + str(invalid_key)}
        return web.Response(text=json.dumps(response_obj), status=500)

    else:
        return web.Response(text=json.dumps(response_obj), status=200)
