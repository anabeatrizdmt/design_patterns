from refrigerated_products import RefrigeratedProducts
from beverages import Beverages


class Factory(object):

    @staticmethod
    def get_product(weight, width, height, category, min_temperature=None, max_temperature=None, min_age=None):

        if category == 'refrigerated_products':
            return RefrigeratedProducts(weight, width, height, category, min_temperature, max_temperature)
        elif category == 'beverages':
            return Beverages(weight, width, height, category, min_age)
