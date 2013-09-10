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
        self.line_items = []

    def add_line_item(self, line_item):
	    self.line_items.append(line_item)
	
    @property
    def total(self):
        if self.line_items:
            prices = [line_item.total for line_item in self.line_items]
            return sum(prices)
        else:
            return 0


class LineItem(object): 
    def __init__(self, item, quantity):
        self.item = item
        self.quantity = quantity

    def __str__(self):
        return '{1}x {0}'.format(self.item, self.quantity) 
    
    @property
    def total(self):
        return self.quantity * self.item.price