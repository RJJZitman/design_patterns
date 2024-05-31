from bank import BankAccount, BankAccountProxy

if __name__ == "__main__":
    permissions = {"deposit": True, "withdraw": False}
    bank_account = BankAccount("Alice", 1000)
    proxy = BankAccountProxy(bank_account, "Bob", permissions)

    proxy.deposit(100)
    proxy.withdraw(50)
