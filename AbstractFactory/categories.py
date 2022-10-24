from products import WholesaleProduct, RetailProduct
from abc import ABC, abstractmethod


class AbstractFactory(ABC):

    @abstractmethod
    def create_product(self, type):
        pass


class RefrigeratedFactory(AbstractFactory):

    def create_product(self, type):
        if type == 'wholesale':
            return WholesaleProduct()
        if type == 'retail':
            return RetailProduct()


class FreshFactory(AbstractFactory):

    def create_product(self, type):
        if type == 'retail':
            return RetailProduct()


class FactoryProducer:

    def get_factory(self, type):
        if type == 'refrigerated':
            return RefrigeratedFactory()
        if type == 'fresh':
            return FreshFactory()
