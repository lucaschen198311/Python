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
            print(f"{amount} has been deposited into account successfully.")
        return self
    def withdraw(self, amount):
        if BankAccount.can_withdraw(self.balance, amount):
            self.balance -= amount
            print(f"{amount} has been withdrawed from account successfully.")
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

class User:
    account_dict = {}
    def __init__(self,name,email, account_type):
        self.name = name
        self.email = email
        self.account_type = account_type
        if self.name not in User.account_dict:
            User.account_dict[self.name] = {}
        self.create_account(self.account_type)
    def create_account(self, account_type):
        if account_type not in User.account_dict[self.name]:
            User.account_dict[self.name][account_type] = BankAccount(int_rate = 0.01, balance = 0)
    def make_deposit(self, amount, account_type):
        if account_type in User.account_dict[self.name]:
            User.account_dict[self.name][account_type].deposit(amount)
        else:
            print("User account doesn't exist.")
    def make_withdrawal(self, amount, account_type):
        if account_type in User.account_dict[self.name]:
            User.account_dict[self.name][account_type].withdraw(amount)
        else:
            print("User account doesn't exist.")
    def display_user_balance(self, account_type):
        if account_type in User.account_dict[self.name]:
            User.account_dict[self.name][account_type].display_account_info()
        else:
            print("User account doesn't exist.")

John = User("John", "john@gmail.com","Checking")
print(John.account_dict)
John.create_account("Saving")
print(John.account_dict)
John.display_user_balance("Checking")
John.display_user_balance("Saving")

John.make_deposit(1000, "Checking")
John.make_deposit(5000, "Saving")

John.display_user_balance("Checking")
John.display_user_balance("Saving")

John.make_withdrawal(100, "Checking")
John.make_withdrawal(500, "Saving")

John.display_user_balance("Checking")
John.display_user_balance("Saving")

