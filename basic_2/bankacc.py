class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        pass

    def withdraw(self, amount):
        if self.balance < amount:
            raise ValueError(f"The sum {amount} is not allowed")
        else:
            self.balance -= amount

    def get_balance(self):
        return self.balance
