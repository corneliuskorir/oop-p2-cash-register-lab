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
        self._discount = discount

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
        self.items.extend([item] * quantity)
        prev = {"item": item, "price": price, "quantity": quantity}
        self.previous_transactions.append(prev)

    def apply_discount(self):
        if not self._discount:
            print("There is no discount to apply.\n")
            return
        discount_total = self.total * (100 - self._discount) / 100
        self.total = (
            int(discount_total) if discount_total.is_integer() else discount_total
        )

        print(f"After the discount, the total comes to ${self.total}.\n")

    def void_last_transaction(self):
        if not self.previous_transactions:
            print("No previous transactions found.")
        void_price = (
            self.previous_transactions[-1]["price"]
            * self.previous_transactions[-1]["quantity"]
        )
        self.total -= void_price
        print(self.total)
        self.previous_transactions.pop()
