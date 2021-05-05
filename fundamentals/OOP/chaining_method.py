class User:
    def __init__(self,name,email,account_number):
        self.name = name
        self.email = email
        self.account_number = account_number
        self.balance = 0
    def make_deposit(self,deposit_amount):
        if deposit_amount < 0:
            print("Please enter correct number.")
        else:
            self.balance += deposit_amount
            print(f"{self.name} has deposited {deposit_amount} into account successfully.")
        return self
    def make_withdrawal(self, withdraw_amount):
        if self.balance < withdraw_amount:
            print("Withdraw exceeds balance and please check")
        else:
            self.balance -= withdraw_amount
            print(f"{self.name} has withdrawed {withdraw_amount} from account successfully.")
        return self
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.balance}")
    def transfer_money(self, other_user, transfer_amount):
        if transfer_amount > self.balance:
            print("Transfer amount exceeds balance and please check.")
        elif transfer_amount <= 0:
            print("Transfer amount can't be negative or zero.")
        elif not other_user:
            print("User to be transfered doesn't exist. Please check username.")
        else:
            self.balance -= transfer_amount
            other_user.balance += transfer_amount
            print(f"{transfer_amount} has been transfered to {other_user.name} successfully.")
        return self

user1 = User("Tom","tom@gmail.com","1234")
user2 = User("John","john@gmail.com","5678")
user3 = User("Amy","amy@gmail.com","91011")
user1.make_deposit(1000).make_deposit(3000).make_deposit(4000).make_withdrawal(2000).display_user_balance()
user2.make_deposit(3000).make_deposit(2500).make_withdrawal(1300).display_user_balance()
user3.make_deposit(2000).make_withdrawal(500).make_withdrawal(1000).make_withdrawal(1500).display_user_balance()
user1.transfer_money(user3, 2000).display_user_balance()
user3.display_user_balance()