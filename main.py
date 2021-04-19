from devices import *
from manager import *


def main():
    a = Keyboard("A-1", "plastic", "Logitech", "China", 200, "Ukraine")
    b = Monitor("B-2", "plastic", "HyperX", "English", 150, "Ukraine")
    d = Monitor("B-3", "iron", "HyperX", "China", 170, "Ukraine")

    objects = [a, b, d]
    manager_object = DeviceManager(objects)

    out1 = manager_object.sort_by_price(False)
    print("sorted by price\n")
    for i in out1:
        print(i)

    out2 = manager_object.search_by_produce("China")
    print("search by produce\n")
    for i in out2:
        print(i)

    out3 = manager_object.search_by_price(200)
    print("search by price\n")
    for i in out3:
        print(i)


if __name__ == "__main__":
    main()

