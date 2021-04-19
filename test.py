import unittest
from manager import *
from devices import *


class TestDevice(unittest.TestCase):

    def setUp(self):
        self.a = Keyboard("A-1", "plastic", "Logitech", "China", 200, "Ukraine")
        self.b = Monitor("B-2", "plastic", "HyperX", "English", 150, 16)
        self.d = Monitor("B-3", "iron", "HyperX", "China", 170, 9)

        objects = [self.a, self.b, self.d]
        self.device_manager = DeviceManager(objects)

    def test_sort_by_price(self):
        self.assertEqual(self.device_manager.sort_by_price(False), [self.b, self.d, self.a])

    def test_search_by_produce(self):
        self.assertEqual(self.device_manager.search_by_produce("English"), [self.b])

    def test_search_by_price_greater_than(self):
        self.assertEqual(self.device_manager.search_by_price_greater_than(180), [self.a])

    def test_sot_by_price_negative(self):
        self.assertNotEqual(self.device_manager.sort_by_price(True), [self.b, self.d, self.a])

    def test_search_by_producer_negative(self):
        self.assertNotEqual(self.device_manager.search_by_produce("China"), [self.b])


