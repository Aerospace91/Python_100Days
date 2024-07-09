"""
Day 42 - Class methods
Create a class for a bank account with methods for deposit and withdrawal.
"""

class Account:
    def __init__(self, accountid, balance):
        self.accountid = accountid
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount <= 0:
            return "Not enough money"
        self.balance -= amount