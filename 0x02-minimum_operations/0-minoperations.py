#!/usr/bin/python3
""" """


def minOperations(n):
    """
    """

    if n < 1:
        return 0
    result = 0
    clipboard = 1
    while n > 1:
        if n % clipboard == 0:
            n //= clipboard
            result += clipboard
        else:
            clipboard += 1
    if n == 1:
        result += clipboard
        return result
    else:
        return 0
