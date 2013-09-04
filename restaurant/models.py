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


class LineItem(object): 
    def __init__(self, item, quantity):
        self.item = item
        self.quantity = quantity
        self.total = quantity * item.price

    def __str__(self):
        return '{1}x {0}'.format(self.item, self.quantity) 

    def __repr__(self):
        return self.__str__()

    def line_total(self):
        return self.total


class Receipt(object):
    def __init__(self):
	self.line_items = []

    def add_line_item(self, line_item):
        self.line_items.append(line_item)

    def __str__():
        pass

    def __repr__():
        return self.__str__()
