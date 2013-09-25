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
        self._tip = 0

    def __str__(self):
        receipt_lines = ['{:21}{:>9}'.format(line_item, '${:,.2f}'.format(line_item.total)) for line_item in self.line_items]
        receipt_lines.append('-' * 30)
        receipt_lines.append('{:21}{:>9}'.format('SUBTOTAL:', '${:,.2f}'.format(self.subtotal)))
        receipt_lines.append('{:21}{:>9}'.format('TAX:', '${:,.2f}'.format(self.tax)))
        receipt_lines.append('{:21}{:>9}'.format('TIP:', '${:,.2f}'.format(self.tip)))
        receipt_lines.append('{:21}{:>9}'.format('TOTAL:', '${:,.2f}'.format(self.total)))
        return '\n'.join(receipt_lines)

    def __repr__(self):
        return self.__str__()

    @property
    def subtotal(self):
        if self.line_items:  #line_items is not None, and is not empty
            prices = [line_item.total for line_item in self.line_items]
            return sum(prices)
        else: 
            return 0

    @property
    def tax(self):
        return self.subtotal * tax_rate / 100

    @property
    def total(self):
        return self.subtotal + self.tax + self.tip

    @property
    def tip(self):
        return self._tip

    def add_tip(self, tip):
        self._tip = tip

    def add_line_item(self, line_item):
        self.line_items.append(line_item)

    def calculate_tip(self, percentage):
        """Calculates the tip from a percentage.

        Arguments:
            percentage -- The percentage for the tip, as a whole number (e.g., 20 = 20%)
        """
        return self.subtotal * percentage / 100


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
