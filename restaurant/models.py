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

    def __str__(self):
        receipt_lines = ['{:21}{:>9}'.format(line_item, '${:,.2f}'.format(line_item.total)) for line_item in self.line_items]
        receipt_lines.append('-' * 30)
        receipt_lines.append('{:21}{:>9}'.format('TOTAL:', '${:,.2f}'.format(self.total)))
        return '\n'.join(receipt_lines)

    def __repr__(self):
        return self.__str__()

    @property
    def total(self):
        if self.line_items:  #line_items is not None, and is not empty
            prices = [line_item.total for line_item in self.line_items]
            return sum(prices)
        else: 
            return 0


class LineItem(object): 
    def __init__(self, item, quantity):
        self.item = item
        self.quantity = quantity

    def __str__(self):
        return '{}x {}'.format(self.quantity, self.item) 

    def __repr__(self):
        return self.__str__()

    @property
    def total(self):
        return self.item.price * self.quantity
