#!/usr/bin/env python3
import sys

# Input comes from standard input (STDIN)
for line in sys.stdin:
    line = line.strip()  # Strip whitespace from the beginning and end of the line
    values = line.split(',')  # Split the CSV line into values assuming it's comma-separated
    if len(values) == 14:  # Adjust this number based on your actual CSV structure
        cls = values[-1].strip()  # Assuming last column is the frequency or class
        print(f"{cls}\t1")  # Emit class and count of 1 for each line
