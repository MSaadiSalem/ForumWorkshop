#!/usr/bin/env python2
# -*- coding: utf-8 -*-


def withdraw(balance, request):
    """Calculating how many currency papers the client required within the ATM machine according to current acount balance.

    Arg:
       balance: Current balance within befor client withdraw operation.
       request: The request a mount by the client.

    Returns:
       balance: The updated account balance after client withdraw operations.
    """

    print "Your current Balance: %d$ \n" % balance

    MONEY_UNITS = [100, 50, 10, 5, 4, 3, 2, 1]
    i = 0

    while request > 0 and request <= balance:
        count = request // MONEY_UNITS[i]
        for j in range(count):
            print "give %s" % MONEY_UNITS[i]
        request -= count * MONEY_UNITS[i]
        balance -= count * MONEY_UNITS[i]
        i += 1

    if request > balance:
        print "The requested money is above your current blance."
    if request < 0:
        print "The requested money is invalid amount."

    return balance


# Test cases
# new_balance = withdraw(500, 277)
# new_balance = withdraw(500, 600)
# new_balance = withdraw(300, 273)
# new_balance = withdraw(500, 500)
# new_balance = withdraw(500, 2)
# new_balance = withdraw(0, 277)
# new_balance = withdraw(500, -20)
new_balance = withdraw(-2, 0)

print "\nThe current balance after operations: %d$ " % new_balance
