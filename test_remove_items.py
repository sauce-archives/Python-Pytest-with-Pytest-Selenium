import pytest


def test_remove_one_item_from_cart(inventory):
    inventory.visit()

    inventory.add_item_to_cart()
    inventory.add_item_to_cart()

    inventory.remove_item_from_cart()

    assert inventory.get_items_in_cart() == '1'