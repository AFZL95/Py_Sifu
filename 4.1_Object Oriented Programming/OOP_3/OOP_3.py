import datetime
import pytz


class Account:
    # this line below is called "Doc String", represents Class's functionality
    # and it necessary for every class that we gonna write !

    """ Simple account class with balance """


    @staticmethod
    # cuz the "_current_time()" method has no attributes,
    # we can implement this method as a static method.
    # IDE detects that the "self" parameter of "_current_time()" method is not used in the declared method
    # which is good bcuz with declaring the method as static,
    # it's stuff not gonna be change in code executing duration
    # so we going to wipe self parameter in parenthesis and add a decoration above the method !
    def _current_time():
        # the variables with one underscore in the start represents the private variables in python
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    # initialization for an instance of the class actually
    # it not gonna happen that U wanna write a class without and init method for it
    # one hundred percent it should be implemented !
    def __init__(self, name, balance):
        # used to set data attributes like name and balance
        self.name = name
        self.balance = balance
        # a list for logging the accounts transactions
        self.transaction_list = []
        print("Account created for " + self.name)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.show_balance()
            self.transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_list.append((Account._current_time(), -amount))
        else:
            print("The amount must be greater than zero and no more then your account balance")
        self.show_balance()

    def show_balance(self):
        print("Balance is {}".format(self.balance))

    def show_transactions(self):
        for date, amount in self.transaction_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print("{:6} {} on {} (local time was {})".format(amount, tran_type, date, date.astimezone()))


if __name__ == '__main__':
    ali = Account("Ali", 0)
    ali.show_balance()

    ali.deposit(1000)

    ali.withdraw(500)

    ali.withdraw(2000)

    # showing the Log
    ali.show_transactions()
