class BankAccount:
    def __init__(self, owner: str, balance: float):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount: float):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")


class BankAccountProxy:
    def __init__(self, bank_account: BankAccount, user: str, permissions: dict[str, bool]):
        self.bank_account = bank_account
        self.user = user
        self.permissions = permissions

    def deposit(self, amount: float):
        if self.permissions.get("deposit", False):
            self.bank_account.deposit(amount)
        else:
            print(f"User {self.user} does not have permission to deposit.")

    def withdraw(self, amount: float):
        if self.permissions.get("withdraw", False):
            self.bank_account.withdraw(amount)
        else:
            print(f"User {self.user} does not have permission to withdraw.")
