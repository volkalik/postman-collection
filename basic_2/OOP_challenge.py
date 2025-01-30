class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f'New deposit ${amount} has been added')

    def withdraw(self, withdraw):
        if self.balance >= withdraw:
            self.balance = self.balance - withdraw
            print(f'you took ${withdraw} from your account')
        else:
            print('Sorry!')
    def __str__(self):
        return f'Owner: {self.owner} \nBalance: {self.balance}'


acct1 = Account('Jose', 100)

print(f'Account owner: {acct1.owner}\n'
      f'Account balance: {acct1.balance}\n')

acct1.deposit(50)
print(f'New account balance: {acct1.balance}')

acct1.withdraw(150)
print(f'Your account balance: {acct1.balance}')
