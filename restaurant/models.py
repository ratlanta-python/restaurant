tax_rate = 8 # in cents

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
    def subtotal(self):
        if self.line_items:  #line_items is not None, and is not empty
            prices = [line_item.total for line_item in self.line_items]
            return sum(prices)
        else: 
            return 0

    @property
    def tax(self):
        tax100 = self.subtotal * tax_rate
        tax = tax100 / 100
        return tax

    @property
    def total(self):
        return self.subtotal + self.tax


class LineItem(object): 
    def __init__(self, item, quantity):
        self.item = item
        self.quantity = quantity

    def __str__(self):
        return '{1}x {0}'.format(self.item, self.quantity) 

    @property
    def total(self):
        return self.item.price * self.quantity
