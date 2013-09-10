import pytest

from restaurant.models import Receipt, LineItem, Item

def test_empty_receipt_total_is_zero():
    receipt = Receipt()
    assert receipt.total == 0
	
def test_receipt_with_single_item_total_equals_item_price():
    receipt = Receipt()
    item = Item('Leinenkugel Creamy Dark Lager', 'Chippewa Falls, WI', 4.00)
    line_item = LineItem(item, 1)
    receipt.add_line_item(line_item)
    assert receipt.total == 4
	
def test_receipt_with_two_items_total_equals_sum_of_item_prices():
    receipt = Receipt()
    item_1 = Item('Leinenkugel Creamy Dark Lager', 'Chippewa Falls, WI', 4.00)
    line_item_1 = LineItem(item_1, 1)
    receipt.add_line_item(line_item_1)
    
    item_2 = Item('Budweiser', 'St. Louis, MO', 3.50)
    line_item_2 = LineItem(item_2, 1)
    receipt.add_line_item(line_item_2)
    assert receipt.total == 7.50
    
def test_receipt_with_multiple_quantity_line_item_total_equals_quantity_times_price():
    receipt = Receipt()
    item = Item('Leinenkugel Creamy Dark Lager', 'Chippewa Falls, WI', 4.00)
    line_item = LineItem(item, 3)
    receipt.add_line_item(line_item)
    assert receipt.total == 12.00
    
def test_line_item_with_multiple_quantity_line_item_total_equals_quantity_times_price():
    item = Item('Leinenkugel Creamy Dark Lager', 'Chippewa Falls, WI', 4.00)
    line_item = LineItem(item, 3)
    assert line_item.total == 12.00