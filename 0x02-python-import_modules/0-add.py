#!/usr/bin/python3
def add(a, b):
    return a + b
if __name__ == "__main__":
    a = 1
    b = 2

    from add_0 import add

    print(f"{a} + {b} = {add(a, b)}")

