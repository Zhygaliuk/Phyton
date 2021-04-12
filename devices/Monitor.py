from devices import Device
from enum import Enum


class Aspect(Enum):
     STANDART = 0
     WIDESCREEN = 1


class Monitor(Device):
    def __init__(self, name, materials, brand, producer, price, size):
        super().__init__(name, materials, brand, producer, price)
        self._size = size

    def __str__(self):
        return f"name: {self._name}\n" \
               f"price: {self._price}\n" \
               f"producer: {self._producer}\n" \
               f"brand: {self._brand}\n" \
               f"materials:{self._materials}\n"\
               f"layout:{self._size}\n"\


    def get_size(self):
        return self._size
