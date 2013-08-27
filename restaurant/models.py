class Restaurant(object):
    pass

class MenuItem(object):
    def __init__(self, name, description, price):
	self.name = name
	self.description = description
	self.price = price

    def __str__(self):
	return self.name

    def __repr__(self):
	self.__str__()

class LineItem(object):
    def __init__(self, item, quantity):
	self.item = item
	self.quantity = quantity

    def __str__(self):
	return '{1}x {0}'.format(self.item, self.quantity)

    def __repr__(self):
	self.__str__()

class Receipt(object):
    def __init__(self):
	pass	
