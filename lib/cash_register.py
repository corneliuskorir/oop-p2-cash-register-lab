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
    def __init__(self, discount=0):
        self.total = 0
        self.items = []
        self.previous_transactions = []
        self.discount = discount

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if type(value) is int and 0 >= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")

    def add_item(self, item, price, quantity=1):
        self.total += price * quantity
        self.items.append(item)
        prev = {"item": item, "price": price, "quantity": quantity}
        self.previous_transactions.append(prev)

    def apply_discount(self):
        if not self.previous_transactions:
            print("There is no discount to apply.")
            return

        self._total = self._total * (100 - self._discount) / 100

    def void_last_transaction(self):
        self.previous_transactions.pop()
