from devices import Device
from enum import Enum


class KeyboardTypes(Enum):
    MEMBRANE = 0
    MECHANICAL = 1
    SEMI = 2


class Keyboard(Device):
    def __init__(self, name, materials, brand, producer, price, layout):
        super().__init__(name, materials, brand, producer, price)
        self._layout = layout

    def __str__(self):
        return f"name: {self._name}\n" \
               f"price: {self._price}\n" \
               f"producer: {self._producer}\n" \
               f"brand: {self._brand}\n" \
               f"materials:{self._materials}\n"\
               f"layout:{self._layout}\n"\


    def get_layout(self):
        return self._layout
