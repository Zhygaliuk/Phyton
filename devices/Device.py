class Device:
    def __init__(self, name, materials, brand, producer, price):
        self._name = name
        self._materials = materials
        self._brand = brand
        self._producer = producer
        self._price = price

    def __str__(self):
        return f"name: {self._name}\n"\
               f"price: {self._price}\n"\
               f"producer: {self._producer}\n"\
               f"brand: {self._brand}\n"\
               f"materials:{self._materials}\n"\


    def get_name(self):
        return self._name

    def get_price(self):
        return self._price

    def get_producer(self):
        return self._producer

    def get_brand(self):
        return self._brand

    def get_materials(self):
        return self._materials




