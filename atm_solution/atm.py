#!/usr/bin/env python2
# -*- coding: utf-8 -*-


def withdraw(limit, request):
    """Calculating how many currency papers the client required within the ATM machine limit.

    Arg:
       limit: Money limit within ATM machine during client withdraw operation.
       withdraw_req: The request a mount by the client.

    Returns:
       new_limit: The updated money limit after client withdraw operations.
    """

    new_limit = limit
    if request > limit:
        print "The requested money is not available at the moment."
        return new_limit

    money_unit = 100
    while request > 0:
        if request - money_unit > 0:
            request -= money_unit
            new_limit -= money_unit
            print "give %s" % money_unit
        elif money_unit == 100:
            money_unit = 50
            continue
        elif money_unit == 50:
            money_unit = 10
            continue
        elif money_unit == 10:
            money_unit = 5
            continue
        else:
            print "give %s" % request
            new_limit -= request
            request = 0
    return new_limit


# Test cases
# new_limit = withdraw(500, 277)
# new_limit = withdraw(500, 600)
# new_limit = withdraw(300, 273)
new_limit = withdraw(500, 2)
# new_limit = withdraw(0, 277)
# new_limit = withdraw(500, -20)
print "The current balance: %d$ " % new_limit
