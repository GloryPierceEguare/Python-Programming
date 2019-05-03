class Item():
    def __init__(self, name, quantity, price):
        self.__name = name
        self.__quantity = quantity
        self.__price = price

    def set_price(self, new_price):
        self.__price = new_price

    def get_price(self):
        return self.__price

    def total_price(self):
        return self.__price * self.__quantity

#Main
#i1 = Item('apples', 10, 0.65)
i2 = Item('orange', 8, 0.85)

#print(i1.total_price())
print(i2.total_price())