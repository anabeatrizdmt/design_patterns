from categories import FactoryProducer

producer = FactoryProducer()
refrigerated_factory = producer.get_factory('refrigerated')
fresh_factory = producer.get_factory('fresh')

refrigerated_wholesale = refrigerated_factory.create_product('wholesale')
refrigerated_retail = refrigerated_factory.create_product('retail')
fresh_retail = fresh_factory.create_product('retail')

print(refrigerated_wholesale.info())
print(refrigerated_retail.info())
print(fresh_retail.info())
