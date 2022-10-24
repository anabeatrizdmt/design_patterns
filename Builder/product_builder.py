class Product:
    def __init__(self, sku):
        self.sku = sku
        self.price = None
        self.category = None
        self.min_age = None
        self.max_temperature = None


class ProductBuilder:
    def __init__(self, sku):
        self.product = Product(sku)

    def set_price(self, value):
        self.product.price = value
        return self

    def set_category(self, value):
        self.product.category = value
        return self

    def set_min_age(self, value):
        self.product.min_age = value
        return self

    def set_max_temperature(self, value):
        self.product.max_temperature = value
        return self

    def build(self):
        return {
            "SKU": self.product.sku,
            "Price": self.product.price,
            "Category": self.product.category,
            "Min_age": self.product.min_age,
            "Max_temperature": self.product.max_temperature
        }
