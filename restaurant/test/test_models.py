import pytest
from restaurant.models import Receipt, LineItem, Item, Category

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

def test_calculated_tax_for_single_item():
    receipt = Receipt()
    item = Item('Leinenkugel Creamy Dark Lager', 'Chippewa Falls, WI', 4.00)
    line_item = LineItem(item, 1)

    receipt.add_line_item(line_item)
    assert receipt.tax == 0.32

def test_calculated_tax_for_multiple_line_items():
    receipt = Receipt()
    item_1 = Item('Leinenkugel Creamy Dark Lager', 'Chippewa Falls, WI', 4.00)
    line_item_1 = LineItem(item_1, 1)
    receipt.add_line_item(line_item_1)
    
    item_2 = Item('Budweiser', 'St. Louis, MO', 3.50)
    line_item_2 = LineItem(item_2, 2)
    receipt.add_line_item(line_item_2)
    assert receipt.tax == 0.88

def test_total_for_empty_receipt_is_zero():
    receipt = Receipt()
    assert receipt.total == 0

def test_total_for_receipt_with_one_item_equals_item_total_and_tax():
    receipt = Receipt()
    item = Item('Leinenkugel Creamy Dark Lager', 'Chippewa Falls, WI', 4.00)
    line_item = LineItem(item, 1)
    receipt.add_line_item(line_item)
    assert receipt.total == 4.32

def test_total_for_receipt_with_multiple_items_is_total_of_items_and_tax():
    receipt = Receipt()
    item = Item('Leinenkugel Creamy Dark Lager', 'Chippewa Falls, WI', 4.00)
    line_item = LineItem(item, 1)
    receipt.add_line_item(line_item)
    
    item_2 = Item('Budweiser', 'St. Louis, MO', 3.50)
    line_item_2 = LineItem(item_2, 2)
    receipt.add_line_item(line_item_2)
    assert receipt.total == 11.88

def test_tip_before_adding_is_zero():
    receipt = Receipt()
    assert receipt.tip == 0

def test_tip_after_adding_is_correct():
    receipt = Receipt()
    item = Item('Leinenkugel Creamy Dark Lager', 'Chippewa Falls, WI', 4.00)
    line_item = LineItem(item, 1)
    receipt.add_line_item(line_item)
    receipt.add_tip(2.00)
    assert receipt.tip == 2.00

def test_receipt_total_after_adding_tip_includes_tip():
    receipt = Receipt()
    item = Item('Leinenkugel Creamy Dark Lager', 'Chippewa Falls, WI', 4.00)
    line_item = LineItem(item, 1)
    receipt.add_line_item(line_item)
    receipt.add_tip(2.00)
    assert receipt.total ==  6.32


def test_calculate_tip_for_empty_receipt_is_zero():
    receipt = Receipt()

    assert receipt.calculate_tip(18) == 0


def test_calculate_tip_for_zero_percent_is_zero():
    receipt = Receipt()
    item = Item('Leinenkugel Creamy Dark Lager', 'Chippewa Falls, WI', 4.00)
    line_item = LineItem(item, 1)
    receipt.add_line_item(line_item)

    assert receipt.total > 0
    assert receipt.calculate_tip(0) == 0


def test_calculate_tip_for_non_empty_receipt_and_positive_percentage_is_correct():
    receipt = Receipt()
    item = Item('Leinenkugel Creamy Dark Lager', 'Chippewa Falls, WI', 4.00)
    line_item = LineItem(item, 1)
    receipt.add_line_item(line_item)    

    assert receipt.calculate_tip(20) == 0.80

def test_item_added_to_empty_category_exists():
    category = Category("Beer")
    item = Item('Leinenkugel Creamy Dark Lager', 'Chippewa Falls, WI', 4.00)

    category.add_item(item);
    assert item in category.items


