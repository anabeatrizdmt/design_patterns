from product_builder import ProductBuilder

arroz1 = ProductBuilder(1023)
arroz1.set_price(9).set_category("Básicos") # como esses estão sempre presentes os colocamos no ProductBuilder()?
print(arroz1.build())

cerveja1 = ProductBuilder(3928)
cerveja1.set_price(5).set_category("Alcoolicos").set_min_age(18)
print(cerveja1.build())

sorvete = ProductBuilder(2938)
sorvete.set_price(35).set_category("Sobremesas").set_max_temperature(-10)
print(sorvete.build())

