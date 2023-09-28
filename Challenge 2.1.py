class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0.0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        return f"Account Balance for {self.__account_holder_name}: ${self.__account_balance:.2f}"
if __name__ == "__main__":
    account = BankAccount("123456", "John Doe", 1000.0)
    if account.deposit(500.0):
        print("Deposit successful!")
    else:
        print("Invalid deposit amount.")
    if account.withdraw(200.0):
        print("Withdrawal successful!")
    else:
        print("Insufficient balance or invalid withdrawal amount.")
    print(account.display_balance())
