#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """Determines if a given data set
    represents a valid utf-8 encoding
    """
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    for byte in data:
        # If we are not inside a UTF-8 character
        if num_bytes == 0:
            # Count the number of bytes in the current character
            if byte >> 7 == 0b0:
                num_bytes = 1
            elif byte >> 5 == 0b110:
                num_bytes = 2
            elif byte >> 4 == 0b1110:
                num_bytes = 3
            elif byte >> 3 == 0b11110:
                num_bytes = 4
            else:
                return False
        else:
            # Check if the current byte follows the format 10xxxxxx
            if byte >> 6 != 0b10:
                return False

        # Decrement the number of expected bytes
        num_bytes -= 1

        # If there are negative bytes or incomplete UTF-8 character
        if num_bytes < 0:
            return False

    # If there are remaining bytes or incomplete UTF-8 character
    return num_bytes == 0
