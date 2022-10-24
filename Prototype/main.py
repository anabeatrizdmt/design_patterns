from abc import ABC, abstractmethod
import copy


class FreshProduct(ABC):
    def __init__(self):
        self.sku = None
        self.price = None
        self.category = "fresh"

    def set_sku(self, value):
        self.sku = value
        return self

    def set_price(self, value):
        self.price = value
        return self

    def clone(self):
        return copy.deepcopy(self)


fresh1 = FreshProduct().set_sku(1001).set_price(10)
print(fresh1.sku)
print(fresh1.price)
print(fresh1.category)

print("\n")

fresh2 = fresh1.clone()
fresh2.set_sku(1002)
print(fresh2.sku)
print(fresh2.price)
print(fresh2.category)