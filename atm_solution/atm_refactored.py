# -*- coding: utf-8 -*-


class ATM():

    def __init__(self, balance, bank_name):
        """Construct an ATM machine object.

        Args:
            balance (int): Current available balance  befor withdraw operation
            bank_name (str): The bank name which ATM machine belongs.
            withdrawals_list (list): Holds the history of withdrawals transactions.
        """

        self.balance = balance
        self.bank_name = bank_name
        self.withdrawals_list = []

    @staticmethod
    def validate_withdraw(request, balance):
        """Checking if the requested amount is valid within the range of the current balance.

        Args:
            request (int): The request a mount by the client.
            balance (int): Current available balance.

        Returns:
            valid (bool): Holds the validity
        """

        valid = True
        if request <= 0:
            print "The requested amount is invalid.\n"
            valid = False
        elif request > balance:
            print "The requested amount is above current balance.\n"
            valid = False
        return valid

    def withdraw(self, request, money_units=[100, 50, 10, 5, 4, 3, 2, 1]):
        """Calculating how many currency papers the client required within the current balance in ATM machine.

        Arg:
           request (int): The request a mount by the client.
           money_units (list): A list of available currency papers.
        """

        print "\n" + "=" * 25 + "\nWelcome to %s\nCurrent balance = %d$\n" % (
            self.bank_name, self.balance) + "=" * 25
        valid = self.validate_withdraw(request, self.balance)
        if valid:
            self.withdrawals_list += [request]

        i = 0
        while request > 0 and valid:
            count = request // money_units[i]
            for j in range(count):
                print "give %s" % money_units[i]
            request -= count * money_units[i]
            self.balance -= count * money_units[i]
            i += 1

    def show_withdrawals(self):
        """Displays the history of withdrawals transactions"""

        print "\n%s ATM Machine Withdrawals Transactions\n" % self.bank_name + "=" * 48
        i = 1
        for withdrawal in self.withdrawals_list:
            print "Withdrawal No.%d amount: %d$" % (i, withdrawal)
            i += 1


# Test cases
balance1, balance2 = 500, 1000
request1, request2 = 277, 1200
atm1 = ATM(balance1, "Smart Bank")
# atm2 = ATM(balance2, "Baraka Bank")
atm1.withdraw(request1)
# atm2.withdraw(request2)

# balance1, balance2 = 500, 500
request1, request2 = 273, 500
atm1.withdraw(request1)
# atm2.withdraw(request2)

# balance1, balance2 = 500, 500
request1, request2 = 100, 300
atm1.withdraw(request1)
# atm2.withdraw(request2)

# balance1, balance2 = 500, 500
request1, request2 = 40, 4
atm1.withdraw(request1)
# atm2.withdraw(request2)

# balance1, balance2 = 500, 500
request1, request2 = 10, 1200
atm1.withdraw(request1)
# atm2.withdraw(request2)

# balance1, balance2 = 500, 0
request1, request2 = 2, 277
atm1.withdraw(request1)
# atm2.withdraw(request2)

# balance1, balance2 = -2, 0
request1, request2 = -3, 0
atm1.withdraw(request1)
# atm2.withdraw(request2)

atm1.show_withdrawals()
