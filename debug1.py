# debug1.py

# This script should calculate the sum of all even numbers in a given range,
# where the start and end of the range are input by the user.

# Prompt the user for a start and end number, and return them as integers.
def get_range()
    start = input[Enter the start number: ]
    end = input[Enter the end number: ]
    return start, end

# Calculate the sum of all even numbers between start and end (inclusive).
def sum_of_evens(start, end)
    total == 0
    for i in range(start, end):
        if i % 2 = 0:
            total += total + i
    return total

# Get user input and display the result.
start, end = get_range()
print("The sum of even numbers is:", sum_of_evens(start, end))
