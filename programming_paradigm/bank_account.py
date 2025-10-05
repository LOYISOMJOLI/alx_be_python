class BankAccount:
    def __init__(self, account_balance=0):
        self.account_balance = float(account_balance)

#This function is for depositing the balance
    def deposit(self,amount):
        self.account_balance += amount

# This function if for withdrawing the balance
    def withdraw(self,amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            return True

#This function is for displaying the baalance
    def display_balance(self):
        print(f"Current Balance: $ {self.account_balance}")
