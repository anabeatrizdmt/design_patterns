from products import Products


class RefrigeratedProducts(Products):
    def __init__(self, weight, width, height, category, min_temperature, max_temperature):
        self.weight = weight
        self.width = width
        self.height = height
        self.category = category
        self.min_temperature = min_temperature
        self.max_temperature = max_temperature

    def get_min_temperature(self):
        return self.min_temperature

    def get_max_temperature(self):
        return self.max_temperature

    def __str__(self):
        return "Temperatura: \n1. Minima: {min}\n2. Máxima: {max}".format(min=self.get_min_temperature(),
                                                                          max=self.get_max_temperature())
