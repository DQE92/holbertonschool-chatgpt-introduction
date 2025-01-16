#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

if len(sys.argv) != 2:
    print("Usage: {} <number>".format(sys.argv[0]))
    sys.exit(1)

try:
    number = int(sys.argv[1])
    if number < 0:
        print("Error: Factorial is not defined for negative numbers.")
        sys.exit(1)
    f = factorial(number)
    print(f)
except ValueError:
    print("Error: Please provide a valid integer.")
    sys.exit(1)