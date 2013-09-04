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
        return '{:,.2f}'.format(self.total)


class Receipt(object):
    def __init__(self):
        self.line_items = []
        self.total = 0

    def add_line_item(self, line_item):
        self.line_items.append(line_item)
        self.total += line_item.total

    def __str__(self):
        receipt_lines = ['{:21}{:>9}'.format(line_item, '${:,.2f}'.format(line_item.total)) for line_item in self.line_items]
        receipt_lines.append('-' * 30)
        receipt_lines.append('{:21}{:>9}'.format('TOTAL:', '${:,.2f}'.format(self.total)))
        return '\n'.join(receipt_lines)

    def __repr__(self):
        return self.__str__()
