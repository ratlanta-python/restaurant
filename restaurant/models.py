class Restaurant(object):
    pass


class Menu(object):
    pass


class Item(object):
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()


class Receipt(object):
    def __init__(self):
        pass


class LineItem(object): 
    def __init__(self, item, quantity):
        self.item = item
        self.quantity = quantity

    def __str__(self):
        return '{1} {0}(s)'.format(self.item, self.quantity) 
