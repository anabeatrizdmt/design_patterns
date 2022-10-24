
class Director:
    __builder = None

    def set_builder(self, builder):
        self.__builder = builder

    def get_product(self):
        product = Product()

        sku = self.__builder.get_sku()
        product.set_sku(sku)

        price = self.__builder.get_price()
        product.set_price(price)

        category = self.__builder.get_category()
        product.set_category(category)


class Product:
    def __init__(self):
        self.__sku = None
        self.__price = None
        self.__category = None

    def set_sku(self, sku):
        self.__sku = sku

    def set_price(self, price):
        self.__price = price

    def set_category(self, category):
        self.__category = category


class Builder:
    def get_sku(self): pass
    def get_price(self): pass
    def get_category(self): pass

