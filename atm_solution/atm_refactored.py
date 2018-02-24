#!/usr/bin/env python2
# -*- coding: utf-8 -*-


def validate_withdraw(balance, request):
    """Checking if the requested amount is valid within the range of the current balance.

    Args:
        balance: Current balance.
        request: The request a mount by the client.

    Returns:
        valid: Holds the validity
    """

    valid = True
    if request <= 0:
        print "The requested money is invalid amount."
        valid = False
    elif request > balance:
        print "The requested money is above your current blance."
        valid = False
    return valid


def withdraw(balance, request, money_units=[100, 50, 10, 5, 4, 3, 2, 1]):
    """Calculating how many currency papers the client required within the ATM machine according to current acount balance.

    Arg:
       balance: Current balance befor client withdraw operation.
       request: The request a mount by the client.
       money_units: A list of available currency papers.

    Returns:
       balance: The updated account balance after client withdraw operations.
    """

    print "Your current Balance: %d$ \n" % balance
    i = 0
    while request > 0:
        count = request // money_units[i]
        for j in range(count):
            print "give %s" % money_units[i]
        request -= count * money_units[i]
        balance -= count * money_units[i]
        i += 1
    print "\nThe current balance after operations: %d$ " % balance
    return balance


# Test cases
# balance, request = 500, 277
# balance, request = 500, 600
# balance, request = 300, 273
# balance, request = 500, 500
# balance, request = 500, 2
# balance, request = 0, 277
# balance, request = 500, -20
# balance, request = -2, 0
balance, request = -2, -3

if validate_withdraw(balance, request):
    withdraw(balance, request)
