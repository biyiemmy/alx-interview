#!/usr/bin/python3
"""
function that determines the number of minimum operations given n characters
"""


def minOperations(n):
    """
    main: function that calculates the fewest number of operations
        needed to give a result of exactly n H characters in a file
    args: n: Number of characters to be displayed
    return: number of min operations - integer
    """

    # all outputs should be at least 2 char: (min, Copy All => Paste)
    if (n < 2):
        return 0
    output, root = 0, 2
    while root <= n:
        # if n evenly divides by root
        if n % root == 0:
            # total even-divisions by root = total operations
            output += root
            # set n to the remainder
            n = n / root
            # reduce root to find remaining smaller vals that evenly-divide n
            root -= 1
        # increment root until it evenly-divides n
        root += 1
    return output

    # """
    # Returns the fewest number of operations needed to result in exactly
    # n H characters in the file.
    # """
    # operations = 0
    # min_operations = 2
    # while n > 1:
    #     while n % min_operations == 0:
    #         operations += min_operations
    #         n /= min_operations
    #     min_operations += 1
    # return operations
