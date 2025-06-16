# debug5.py

# This script defines a simple BankAccount class that supports deposit and withdrawal,
# and prints a transaction history after a few simulated operations.

# Class to represent a bank account with basic transaction capabilities.
class BankAccount:
    def __init__(self, owner, balance=0):
        # Initialize account with owner name and starting balance.
        self.owner = owner
        self.balance = balance
        self.transactions = []

    # Add funds to the account and record the transaction.
    def deposit(self, amount):
        if amount <= 0:
            print("Deposit must be positive.")
            return
        self.balance += amount
        self.transactions.append(f"Deposited ${amount}")

    # Withdraw funds if sufficient balance exists; otherwise, print error.
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
            return
        self.balance -= amount
        self.transactions.append(f"Withdrew ${amount}")

    # Print account summary, including all transactions.
    def print_summary(self):
        print(f"Account owner: {self.owner}")
        print(f"Current balance: ${self.balance}")
        print("Transactions:")
        for t in self.transactions:
            print("-", t)

# Main function to simulate deposits, withdrawals, and print the account summary.
def main():
    acct = BankAccount("Alice", 100)
    acct.deposit(50)
    acct.withdraw(30)
    acct.withdraw(150)
    acct.print_summary()

main()
