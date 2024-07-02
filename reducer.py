#!/usr/bin/env python3
import sys

current_class = None
current_count = 0

# Input comes from standard input (STDIN)
for line in sys.stdin:
    line = line.strip()  # Strip whitespace from the beginning and end of the line
    cls, count = line.split('\t')  # Split line into class and count
    count = int(count)  # Convert count to integer

    # Check if current_class is the same as cls from input
    if current_class == cls:
        current_count += count  # Increment count for current class
    else:
        # If current_class is not None, print the class and its total count
        if current_class is not None:
            print(f"{current_class}\t{current_count}")  # Output the class and count
        current_class = cls  
        current_count = count  # Reset count for the new class

# output the last class encountered
if current_class is not None:
    print(f"{current_class}\t{current_count}")
