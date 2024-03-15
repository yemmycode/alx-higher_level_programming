#!/usr/bin/python3
import sys

def main():
    num_args = len(sys.argv) - 1

    print(f"Number of argument(s): {num_args}")

    plural_suffix = 's' if num_args != 1 else ''

    separator = ':'

    print(f"Argument{plural_suffix} {separator}")

    for i, arg in enumerate(sys.argv[1:], start=1):
        print(f"{i}: {arg}")

if __name__ == "__main__":
    main()
