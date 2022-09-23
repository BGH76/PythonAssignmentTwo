
class BankAccount:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance


    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdrawl(self, amount):
        self.balance = self.balance - amount

    def bank_fees(self):
        self.balance = self.balance - (self.balance * .05)

    def display_account_details(self):
        print("Name: " + self.name + "\n" +
              "Account Number: " + str(self.account_number) + "\n" +
              "Balance: " + str(self.balance))