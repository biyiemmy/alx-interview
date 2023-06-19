#!/usr/bin/python3
"""
Main file - 0-making_change.py
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values,
    determine the fewest number of coins needed to meet
    a given amount total.
    """
    if total <= 0:
        return 0

    # initialize a list to track the fewest coins needed for each total
    minimum_coins = [float('inf')] * (total + 1)
    minimum_coins[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                # calculate the fewest coins needed for the current total
                # by taking the minimum of the previous fewest coins needed
                # for i and the fewest coins needed for i - coin plus 1
                # (since we are using one coin)
                minimum_coins[i] = min(
                    minimum_coins[i], minimum_coins[i - coin] + 1)

    if minimum_coins[total] == float('inf'):
        # if the fewest coins needed for the total is still infinity,
        # it means the total cannot be met by any number of coins
        return -1
    else:
        return minimum_coins[total]
