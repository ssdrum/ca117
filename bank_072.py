#!/usr/bin/env python3

class BankAccount(object):
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount

    def __str__(self):
        return f"Your current balance is {self.balance:.2f} euro"

def main():
    b1 = BankAccount(300)
    b1.withdraw(400)


if __name__ == "__name__":
    main()