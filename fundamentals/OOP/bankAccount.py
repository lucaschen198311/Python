class BankAccount:
    account_record = []
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate = 0.01, balance = 0): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.account_record.append(self)
    def deposit(self, amount):
        if amount < 0:
            print("Please enter correct number.")
        else:
            self.balance += amount
        return self
    def withdraw(self, amount):
        if BankAccount.can_withdraw(self.balance, amount):
            self.balance -= amount
        else:
            print("Insufficient balance to withdraw: Charging a $5 fee")
            self.balance -= 5
        return self
    def display_account_info(self):
        print(f"The account balance is {self.balance}.")
    def yield_interest(self):
        if self.balance>0:
            self.balance += self.balance*self.int_rate
        return self
    @staticmethod
    def can_withdraw(balance,amount):
        if balance>=amount:
            return True
        else:
            return False
    @classmethod
    def print_account_info(cls):
        for account in cls.account_record:
            print(f"Balance: {account.balance}, interest_rate: {account.int_rate}")
        
account1 = BankAccount(0.02,100)
account2 = BankAccount()
account1.deposit(1000).deposit(500).deposit(1100).withdraw(500).yield_interest().display_account_info()
account2.deposit(600).deposit(700).withdraw(300).withdraw(600).withdraw(100).withdraw(500).yield_interest().display_account_info()

BankAccount.print_account_info()