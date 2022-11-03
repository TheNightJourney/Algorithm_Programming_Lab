from ClassFolder import BankAccount
from ClassFolder import User


def transaction(item, user):
    if user.pay(item):
        return "Transaction Complete"
    else:
        return "Transaction Failed"

restaurant = {

    "burger": 10,
    "soft drink": 5
}

bookstore = {
    "comic": 10,
    "magazine": 7,
    "textbook": 50,

}

john = User("John",50)
print(transaction(restaurant["burger"], john))
print(transaction(restaurant["soft drink"], john))
print(transaction(bookstore["comic"], john))
print(transaction(bookstore["textbook"], john))
john.deposit(50)
print(transaction(bookstore["textbook"], john))