import pytest
from restaurant.models import Receipt, LineItem, Item

def test_empty_receipt_test_subtotal_is_zero():
    receipt = Receipt()

    assert receipt.subtotal == 0


def test_receipt_with_single_item_subtotal_equals_item_price():
    receipt = Receipt()
    item = Item('Leinenkugel Creamy Dark Lager', 'Chippewa Falls, WI', 4.00)
    line_item = LineItem(item, 1)

    receipt.add_line_item(line_item)
    assert receipt.subtotal == 4.00

def test_receipt_with_two_items_subtotal_equals_sum_of_item_prices():
    receipt = Receipt()
    item_1 = Item('Leinenkugel Creamy Dark Lager', 'Chippewa Falls, WI', 4.00)
    line_item_1 = LineItem(item_1, 1)
    receipt.add_line_item(line_item_1)
    
    item_2 = Item('Budweiser', 'St. Louis, MO', 3.50)
    line_item_2 = LineItem(item_2, 1)
    receipt.add_line_item(line_item_2)

    assert receipt.subtotal == 7.50   
    
def test_receipt_with_multiple_quanity_line_item_subtotal_equals_quantity_times_price():
    receipt = Receipt()
    item = Item('Leinenkugel Creamy Dark Lager', 'Chippewa Falls, WI', 4.00)
    line_item = LineItem(item, 3)
    receipt.add_line_item(line_item)
    assert receipt.subtotal == 12.00

def test_line_item_multiple_quantity_total_equals_quantity_times_price():
    item = Item('Leinenkugel Creamy Dark Lager', 'Chippewa Falls, WI', 4.00)
    line_item = LineItem(item, 3)
    assert line_item.total == 12.00

def test_calculated_tax_for_empty_receipt_is_zero():
    receipt = Receipt()

    assert receipt.tax == 0


def text_calculated_tax_for_single_item():
    receipt = Receipt()
    item = Item('Leinenkugel Creamy Dark Lager', 'Chippewa Falls, WI', 4.00)
    line_item = LineItem(item, 1)

    receipt.add_line_item(line_item)
    assert receipt.tax == 0.32


