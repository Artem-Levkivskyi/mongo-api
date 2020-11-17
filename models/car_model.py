from mongoengine import *
import settings

connect(settings.MONGO_DB_NAME)


class Car(Document):
    manufacturer = StringField(max_length=15)
    model = StringField(max_length=15)
    year = StringField(max_length=4)
    colour = StringField(max_length=15)
    vin = StringField(unique=True, max_length=17)

    def __init__(self, manufacturer, model, year, colour, vin, *args, **values):
        super().__init__()
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.colour = colour
        self.vin = vin

    @staticmethod
    async def create(to_make):
        Car(to_make['manufacturer'], to_make['model'], to_make['year'], to_make['colour'], to_make['vin']).save()
        return {'Status': 'success'}

    @staticmethod
    async def find(to_find):
        cars = Car.objects(__raw__=to_find)
        result = []
        for car in cars:
            result.append({'manufacturer': car['manufacturer'], 'model': car['model'], 'year': car['year'], 'colour': car['colour'], 'vin': car['vin']})
        return tuple(result)

    @staticmethod
    async def update(to_update):
        to_update = dict(to_update)
        vin = to_update['vin']
        to_update.pop('vin', None)
        Car.objects(vin=vin).update(**to_update)
        return {'Status': 'Success'}

    @staticmethod
    async def drop(to_delete):
        Car.objects(__raw__=to_delete).delete()
        return {'Status': 'success'}
