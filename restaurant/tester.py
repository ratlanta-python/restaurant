class Tester(object):

    def __init__(self):
        from restaurant import models
        self.item = models.Item('Test', 'An example item', 4.23)
        self.line_item = models.LineItem(self.item, 12)
        self.receipt = models.Receipt()
        self.receipt.add_line_item(self.line_item)
