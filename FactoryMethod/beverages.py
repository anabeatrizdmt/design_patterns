from products import Products


class Beverages(Products):
    def __init__(self, weight, width, height, category, min_age):
        self.weight = weight
        self.width = width
        self.height = height
        self.category = category
        self.min_age = min_age

    def get_min_age(self):
        return self.min_age

    def __str__(self):
        return "Idade mínima para comprar: {min}".format(min=self.get_min_age())
