class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def get_balance(self):
        print(self.balance)

    def deposit(self, top_up_sum):
        self.balance += top_up_sum
        return True

    def pay(self, payment_sum):
        if self.balance >= payment_sum:
            self.balance -= payment_sum
            return True
        else:
            return False


class User:

    def __init__(self, username, initial_balance):
        self.username = username
        self.__Bank_Account = BankAccount(initial_balance)

    def get_balance(self):
        return self.__Bank_Account.get_balance()

    def deposit(self, deposit_amount):
        return self.__Bank_Account.deposit(deposit_amount)

    def pay(self, payment_amount):
        return self.__Bank_Account.pay(payment_amount)











