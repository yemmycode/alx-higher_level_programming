#!/usr/bin/python3

import sys
from calculator_1 import add, sub, mul, div

def main():
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a, operator, b = sys.argv[1], sys.argv[2], sys.argv[3]

    try:
        a, b = int(a), int(b)
    except ValueError:
        print("Invalid input. Please enter valid integers for <a> and <b>.")
        sys.exit(1)

    if operator == '+':
        result = add(a, b)
    elif operator == '-':
        result = sub(a, b)
    elif operator == '*':
        result = mul(a, b)
    elif operator == '/':
        if b == 0:
            print("Error: Division by zero is not allowed.")
            sys.exit(1)
        result = div(a, b)
    else:
        print(f"Unknown operator '{operator}'. Available operators: +, -, *, and /")
        sys.exit(1)

    print(f"{a} {operator} {b} = {result}")

if __name__ == "__main__":
    main()
