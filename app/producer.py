import asyncio
import sys
import datetime as dt

from os import environ

from random import uniform, randrange


class Producer:

    def __init__(self, connection):
        self.connection = connection

    async def send_data(self):
        while True:
            await asyncio.sleep(1)
            print("Task Executed")
            try:
                today = dt.datetime.now()
                timestamp = today.strftime("%d-%m-%Y %H:%M:%S")
                data = {
                    'device_id': Producer.get_meter_id(),
                    'measure_value': Producer.get_measures(),  # Medida aleatoria
                    'measure_unit': environ.get('measure_unit'),
                    'measure_date': timestamp
                }
                resp = self.connection.xadd('RMSystem', data)
                print(data)
                print(resp)

            except ConnectionError as e:
                print("ERROR REDIS CONNECTION: {}".format(e))
            except Exception as e:
                print('ERROR NO CONTROLADO: {}'.format(str(e)))
                sys.exit()

    @staticmethod
    def get_measures():
        """
        generar medida aleatoria en un rango
        """
        value = uniform(10, 100)
        rounded_value = round(value, 2)
        return rounded_value

    @staticmethod
    def get_meter_id():
        """
        generar id aleatorio de un medidor entre 1 y 5
        """
        return randrange(1, 3)
