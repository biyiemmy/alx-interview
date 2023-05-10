#!/usr/bin/env python3

"""Script that reads stdin line by line and computes metrics"""

import sys

# Define variables to hold metrics
total_size = 0
status_counts = {}

# Define function to print statistics


def print_statistics():
    """ prints information """
    print(f"File size: {total_size}")
    for status_code in sorted(status_counts.keys()):
        print(f"{status_code}: {status_counts[status_code]}")


# Read input lines from stdin
for i, line in enumerate(sys.stdin):
    try:
        # Parse input line
        ip, _, _, date, _, request, status, size = line.split()

        # Compute metrics
        total_size += int(size)
        status_counts[status] = status_counts.get(status, 0) + 1

        # Print statistics every 10 lines or at keyboard interruption
        if (i + 1) % 10 == 0:
            print_statistics()
    except ValueError:
        # Skip invalid input lines
        continue

# Print final statistics
print_statistics()
