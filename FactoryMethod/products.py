class Products(object):

    def __init__(self):
        self.weight = None
        self.width = None
        self.height = None
        self.category = None


    def get_weight(self):
        return self.weight

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_category(self):
        return self.category

    def __str__(self):
        return "Informação de um produto: \n1. Categoria: {c}\n2. Peso: {p}\n3. Largura: {l}\n4. Altura: {a}".format(p=self.get_weight(),
                                                                                                  l=self.get_width(),
                                                                                                  a=self.get_height(),
                                                                                                  c=self.get_category())
