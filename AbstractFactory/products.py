from abc import ABC, abstractmethod


class Product(ABC):
    @abstractmethod
    def info(self): # poderia ser price(self)?
        pass


class WholesaleProduct(Product):
    def info(self):
        return self.__class__.__name__


class RetailProduct(Product):
    def info(self):
        return self.__class__.__name__
