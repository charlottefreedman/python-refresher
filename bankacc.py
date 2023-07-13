class MyBankAccount:
    # initializing variables
    def __init__(self, name, balance, accnum):
        self.accnum = accnum
        self.name = name
        self._balance = balance

    # method to take money out of bank account
    def withdraw(self, amount):
        # makes negative balance impossible
        if amount <= self._balance:
            self._balance -= amount
            print("Remaining balance: " + str(self._balance))
            return self._balance
        else:
            raise ValueError("Insufficient balance")

    # method to deposit money into bank account
    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Unable to deposit a negative value")
        else:
            self._balance += amount
            print("Updated balance: " + str(self._balance))
            return self._balance

    def print_balance(self):
        print(
            f"Account Number: {self.accnum} \nName: {self.name} \nBalance: {self.balance}"
        )


# if __name__ == "__main__":
