#!/usr/bin/env python2
# -*- coding: utf-8 -*-


def withdraw(limit, request):
    """Calculating how many currency papers the client required within the ATM machine limit.

    Arg:
       limit: Money limit within ATM machine during client withdraw operation.
       withdraw_req: The request a mount by the client.

    Returns:
       limit: The updated money limit after client withdraw operations.
    """

    money_unit = 100
    while request > 0 and request <= limit:
        if request - money_unit >= 0:
            request -= money_unit
            limit -= money_unit
            print "give %s" % money_unit
        elif money_unit == 100:
            money_unit = 50
        elif money_unit == 50:
            money_unit = 10
        elif money_unit == 10:
            money_unit = 5
        else:
            print "give %s" % request
            limit -= request
            request = 0

    if request > limit:
        print "The requested money is above the current blance."
    if request < 0:
        print "The requested money is invalid amount."

    return limit


# Test cases
# new_limit = withdraw(500, 277)
# new_limit = withdraw(500, 600)
# new_limit = withdraw(300, 273)
# new_limit = withdraw(500, 500)
# new_limit = withdraw(500, 2)
# new_limit = withdraw(0, 277)
new_limit = withdraw(500, -20)

print "The current balance: %d$ " % new_limit
