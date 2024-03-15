#!/usr/bin/python3

import sys

def main():
    args = sys.argv[1:] 
    total = 0

    for arg in args:
        try:
            total += int(arg)
        except ValueError:
            print("Error: All arguments must be integers.")
            return

    print(total)

if __name__ == "__main__":
    main()
