class DeviceManager:
    def __init__(self, device=list):
        self.__device = device

    def sort_by_price(self, order):

        self.__device.sort(key=lambda n: n.get_price(), reverse=order)
        return self.__device

    def search_by_produce(self, producer):
        out = list()
        for i in self.__device:
            if i.get_producer() == producer:
                out.append(i)
        return out

    def search_by_price(self, price):
        out = list()
        for i in self.__device:
            if i.get_price() == price:
                out.append(i)
        return out
