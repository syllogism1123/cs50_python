class Account:
    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount


def main():
    acc = Account()
    print("Balance: ${:,.2f}".format(acc.balance))
    acc.deposit(100)
    acc.withdraw(50)
    print("Balance: ${:,.2f}".format(acc.balance))


if __name__ == "__main__":
    main()
