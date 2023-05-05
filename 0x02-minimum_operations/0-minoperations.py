#!/usr/bin/python3
"""
function that determines the number of minimum operations given n characters
"""


def minOperations(n):
    """
    main: function that calculates the fewest number of operations
        needed to give a result of exactly n H characters in a file
    args: n: Number of characters to be displayed
    return: number of min operations
    """

    if n <= 1:
        return 0

    # initialize the DP table
    dp = [float('inf')] * (n + 1)
    dp[1] = 0

    # fill the DP table
    for i in range(2, n + 1):
        for j in range(1, i):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + (i // j))

    return dp[n]
