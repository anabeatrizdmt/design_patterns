import products
import factory

if __name__ == '__main__':
    my_factory = factory.Factory()

    product1 = my_factory.get_product(1, 10, 20, 'refrigerated_products', -5, 3, None)
    print(product1)

    product2 = my_factory.get_product(1, 10, 20, 'beverages', None, None, 18)
    print(product2)

