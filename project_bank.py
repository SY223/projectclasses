from decimal import Decimal


class Account:
    def __init__(self, account_number, account_type, balance, account_holder):
        if len(str(account_number)) > 10:
            raise ValueError("Account number cannot exceed 10 digits.")
        self.account_number = account_number
        self.account_type = account_type
        self.balance = Decimal(str(balance))
        self.account_holder = account_holder

    def deposit(self, amount):
        self.balance += Decimal(str(amount))
    
    def withdraw(self, amount):
        amount = Decimal(str(amount))
        if amount > self.balance:
            raise ValueError("Dear customer, you do not have enough money to process this transaction.")
        self.balance -= amount

    def get_balance(self):
        return self.balance

    def get_acount_number(self):
        return self.account_number

    def get_account_type(self):
        return self.account_type

    def get_account_details(self):
        return {
            "Account Name": self.account_holder,
            "Account Type": self.account_type,
            "Account Number": self.account_number,
            "Balance": self.balance
        }

class SavingsAccount(Account):
    def get_account_details(self):
        return {
            "Account Name": self.account_holder,
            "Account Type": self.account_type,
            "Account Number": self.account_number,
            "Balance": self.balance,
            "Account Benefits": "Earns quarterly interest over time"
        }

class CurrentAccount(Account):
    def get_account_details(self):
        return {
            "Account Name": self.account_holder,
            "Account Type": self.account_type,
            "Account Number": self.account_number,
            "Balance": self.balance,
            "Account Benefits": "Allows overdraft facility"
        }

customer_one = SavingsAccount(1297784537, "Savings", 300200.89, "Bailey Gumfrost")
account_number = customer_one.get_acount_number()
registered_holder = customer_one.account_holder
print("Your balance is £" + str(customer_one.get_balance()))
print("Account Number: " + str(account_number))
print("Account Holder: " + registered_holder)