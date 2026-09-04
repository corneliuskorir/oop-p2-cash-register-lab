#!/usr/bin/env python3

"""
cash reg object
add items
apply discounts
void previous transactions
attr: discount, total, items, previous_transactions
methods: add_item(item, price, quantity), apply_discount(), void_last_transaction()
"""


class CashRegister:
    def __init__(self):
        self._total = 0
        self._items = []
        self._previous_transactions = []
        self._discount = 0

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if type(value) is int and 0 >= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")

    def add_item(self, item, price, quantity):
        self._total += price * quantity
        self._items.append(item)
        prev = {"item": item, "price": price, "quantity": quantity}
        self._previous_transactions.append(prev)

    def apply_discounts(self):
        if not self._previous_transactions:
            print("There is no discount to apply.")
            return

        self._total = self._total * (100 - self._discount) / 100

    def void_last_transaction(self):
        self._previous_transactions.pop()
