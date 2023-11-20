#!/usr/bin/env python3
# Created by: Finn Kitor
# Created on: November 20th, 2023
# This program generates different values between 1000 to 2000 using loops and if statements.
# it will generate numbers across by 5


def main() -> None:
    # Initialize a counter to keep track of the number of integers printed on each line
    count = 0

    # Go through the range of numbers from 1000 to 2000
    for num in range(1000, 2001):
        # Check if the count is equal to 5
        if count == 5:
            # If count is equal to 5, print a new line and reset the count to 0
            print()
            count = 0

        # Print the current number followed by a space
        print(num, end=" ")

        # Increment the count by 1
        count += 1


if __name__ == "__main__":
    main()
